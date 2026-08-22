/**
 * Sensirion SHT30 / SHT31 High-Precision Temperature and Humidity I2C Driver
 */

#ifndef SHT30_AIR_SENSOR_H
#define SHT30_AIR_SENSOR_H

#include <Arduino.h>
#include <Wire.h>

struct AmbientAirReading {
    float temperatureCelsius;
    float relativeHumidityPct;
    float dewPointCelsius;
    float vaporPressureDeficitKpa;
    bool isValid;
};

class SHT30AirSensor {
private:
    uint8_t _i2cAddress;
    TwoWire* _wire;

    uint8_t calculateCRC8(const uint8_t* data, int len) {
        uint8_t crc = 0xFF;
        for (int j = 0; j < len; j++) {
            crc ^= data[j];
            for (int i = 8; i > 0; --i) {
                if (crc & 0x80) {
                    crc = (crc << 1) ^ 0x31;
                } else {
                    crc = (crc << 1);
                }
            }
        }
        return crc;
    }

public:
    SHT30AirSensor(uint8_t i2cAddress = 0x44, TwoWire* wire = &Wire)
        : _i2cAddress(i2cAddress), _wire(wire) {}

    bool begin(int sdaPin = 21, int sclPin = 22, uint32_t frequency = 100000) {
        _wire->begin(sdaPin, sclPin, frequency);
        return true;
    }

    bool readData(AmbientAirReading& reading) {
        // Send high-repeatability measurement command with clock stretching disabled (0x2400)
        _wire->beginTransmission(_i2cAddress);
        _wire->write(0x24);
        _wire->write(0x00);
        if (_wire->endTransmission() != 0) {
            reading.isValid = false;
            return false;
        }

        delay(20); // Measurement duration

        uint8_t bytesReceived = _wire->requestFrom((int)_i2cAddress, 6);
        if (bytesReceived != 6) {
            reading.isValid = false;
            return false;
        }

        uint8_t data[6];
        for (int i = 0; i < 6; i++) {
            data[i] = _wire->read();
        }

        // Verify CRCs
        if (calculateCRC8(&data[0], 2) != data[2] || calculateCRC8(&data[3], 2) != data[5]) {
            reading.isValid = false;
            return false;
        }

        uint16_t rawTemp = (data[0] << 8) | data[1];
        uint16_t rawHum = (data[3] << 8) | data[4];

        reading.temperatureCelsius = -45.0f + (175.0f * (float)rawTemp / 65535.0f);
        reading.relativeHumidityPct = 100.0f * ((float)rawHum / 65535.0f);

        // Calculate Dew Point (Magnus formula)
        float a = 17.27f;
        float b = 237.7f;
        float alpha = ((a * reading.temperatureCelsius) / (b + reading.temperatureCelsius)) + log(reading.relativeHumidityPct / 100.0f);
        reading.dewPointCelsius = (b * alpha) / (a - alpha);

        // Calculate Vapor Pressure Deficit (VPD in kPa)
        float es = 0.61078f * exp((17.27f * reading.temperatureCelsius) / (reading.temperatureCelsius + 237.3f));
        float ea = es * (reading.relativeHumidityPct / 100.0f);
        reading.vaporPressureDeficitKpa = max(0.0f, es - ea);

        reading.isValid = true;
        return true;
    }
};

#endif // SHT30_AIR_SENSOR_H
