/**
 * Modbus RS-485 7-in-1 Soil Multi-Parameter Probe Driver
 * Measures: Volumetric Soil Moisture, Temperature, Electrical Conductivity (EC),
 * Soil pH, Nitrogen (N), Phosphorus (P), and Potassium (K).
 */

#ifndef MODBUS_NPK_7IN1_H
#define MODBUS_NPK_7IN1_H

#include <Arduino.h>
#include <HardwareSerial.h>

struct SoilNutrientProfile {
    float moisturePct;
    float temperatureC;
    uint16_t electricalConductivityUsCm;
    float phLevel;
    uint16_t nitrogenMgKg;
    uint16_t phosphorusMgKg;
    uint16_t potassiumMgKg;
    uint32_t sampleTimestampMs;
    bool validCRC;
};

class ModbusNPK7in1Sensor {
private:
    HardwareSerial* _serial;
    uint8_t _deRePin;
    uint8_t _slaveAddress;
    uint32_t _baudRate;
    
    static const uint8_t READ_HOLDING_REGISTERS = 0x03;
    static const uint16_t START_REGISTER = 0x0000;
    static const uint16_t REGISTER_COUNT = 0x0007;
    
    uint16_t calculateCRC16(const uint8_t* buffer, uint16_t length) {
        uint16_t crc = 0xFFFF;
        for (uint16_t pos = 0; pos < length; pos++) {
            crc ^= (uint16_t)buffer[pos];
            for (int i = 8; i != 0; i--) {
                if ((crc & 0x0001) != 0) {
                    crc >>= 1;
                    crc ^= 0xA001;
                } else {
                    crc >>= 1;
                }
            }
        }
        return crc;
    }

public:
    ModbusNPK7in1Sensor(HardwareSerial* serialPort, uint8_t deRePin, uint8_t slaveAddress = 0x01, uint32_t baudRate = 9600)
        : _serial(serialPort), _deRePin(deRePin), _slaveAddress(slaveAddress), _baudRate(baudRate) {}

    void begin(int rxPin = 16, int txPin = 17) {
        pinMode(_deRePin, OUTPUT);
        digitalWrite(_deRePin, LOW); // Receive mode default
        _serial->begin(_baudRate, SERIAL_8N1, rxPin, txPin);
    }

    bool querySensor(SoilNutrientProfile& profile) {
        uint8_t queryFrame[8];
        queryFrame[0] = _slaveAddress;
        queryFrame[1] = READ_HOLDING_REGISTERS;
        queryFrame[2] = (START_REGISTER >> 8) & 0xFF;
        queryFrame[3] = START_REGISTER & 0xFF;
        queryFrame[4] = (REGISTER_COUNT >> 8) & 0xFF;
        queryFrame[5] = REGISTER_COUNT & 0xFF;
        
        uint16_t crc = calculateCRC16(queryFrame, 6);
        queryFrame[6] = crc & 0xFF;
        queryFrame[7] = (crc >> 8) & 0xFF;

        // Clear RX FIFO
        while (_serial->available()) {
            _serial->read();
        }

        // Transmit Frame
        digitalWrite(_deRePin, HIGH);
        delayMicroseconds(500);
        _serial->write(queryFrame, sizeof(queryFrame));
        _serial->flush();
        digitalWrite(_deRePin, LOW);
        delayMicroseconds(500);

        // Await response (19 bytes expected: Addr(1) + Func(1) + ByteCount(1) + Data(14) + CRC(2))
        uint8_t rxBuffer[32];
        uint8_t bytesRead = 0;
        uint32_t startTime = millis();

        while (millis() - startTime < 350) {
            if (_serial->available()) {
                rxBuffer[bytesRead++] = _serial->read();
                if (bytesRead >= 19) break;
            }
        }

        if (bytesRead < 19) {
            profile.validCRC = false;
            return false;
        }

        // Verify CRC
        uint16_t expectedCRC = (rxBuffer[18] << 8) | rxBuffer[17];
        uint16_t computedCRC = calculateCRC16(rxBuffer, 17);
        if (expectedCRC != computedCRC) {
            profile.validCRC = false;
            return false;
        }

        // Parse 16-bit register values
        profile.moisturePct = (float)((rxBuffer[3] << 8) | rxBuffer[4]) / 10.0f;
        int16_t rawTemp = (int16_t)((rxBuffer[5] << 8) | rxBuffer[6]);
        profile.temperatureC = (float)rawTemp / 10.0f;
        profile.electricalConductivityUsCm = (rxBuffer[7] << 8) | rxBuffer[8];
        profile.phLevel = (float)((rxBuffer[9] << 8) | rxBuffer[10]) / 10.0f;
        profile.nitrogenMgKg = (rxBuffer[11] << 8) | rxBuffer[12];
        profile.phosphorusMgKg = (rxBuffer[13] << 8) | rxBuffer[14];
        profile.potassiumMgKg = (rxBuffer[15] << 8) | rxBuffer[16];
        profile.sampleTimestampMs = millis();
        profile.validCRC = true;

        return true;
    }
};

#endif // MODBUS_NPK_7IN1_H
