/**
 * Cayenne Low Power Payload (LPP) Binary Serializer
 * Encodes multi-sensor telemetry into ultra-compact byte payloads for LoRaWAN transmission.
 */

#ifndef CAYENNE_LPP_ENCODER_H
#define CAYENNE_LPP_ENCODER_H

#include <Arduino.h>

#define LPP_DIGITAL_INPUT       0   // 1 byte
#define LPP_DIGITAL_OUTPUT      1   // 1 byte
#define LPP_ANALOG_INPUT        2   // 2 bytes, 0.01 signed
#define LPP_ANALOG_OUTPUT       3   // 2 bytes, 0.01 signed
#define LPP_LUMINOSITY          101 // 2 bytes, 1 lux unsigned
#define LPP_PRESENCE            102 // 1 byte
#define LPP_TEMPERATURE         103 // 2 bytes, 0.1 degC signed
#define LPP_RELATIVE_HUMIDITY   104 // 1 byte, 0.5% unsigned
#define LPP_ACCELEROMETER       113 // 6 bytes, 0.001G signed
#define LPP_BAROMETER           115 // 2 bytes, 0.1 hPa unsigned
#define LPP_VOLTAGE             116 // 2 bytes, 0.01 V unsigned
#define LPP_CURRENT             117 // 2 bytes, 0.001 A unsigned
#define LPP_POWER               128 // 2 bytes, 1 W unsigned

class CayenneLPPEncoder {
private:
    uint8_t* _buffer;
    uint8_t _maxSize;
    uint8_t _cursor;

public:
    CayenneLPPEncoder(uint8_t maxSize = 64) : _maxSize(maxSize), _cursor(0) {
        _buffer = (uint8_t*)malloc(maxSize);
    }

    ~CayenneLPPEncoder() {
        if (_buffer) free(_buffer);
    }

    void reset() {
        _cursor = 0;
    }

    uint8_t getSize() const {
        return _cursor;
    }

    const uint8_t* getBuffer() const {
        return _buffer;
    }

    bool addTemperature(uint8_t channel, float celsius) {
        if (_cursor + 4 > _maxSize) return false;
        int16_t val = (int16_t)(celsius * 10.0f);
        _buffer[_cursor++] = channel;
        _buffer[_cursor++] = LPP_TEMPERATURE;
        _buffer[_cursor++] = (val >> 8) & 0xFF;
        _buffer[_cursor++] = val & 0xFF;
        return true;
    }

    bool addRelativeHumidity(uint8_t channel, float rhPct) {
        if (_cursor + 3 > _maxSize) return false;
        uint8_t val = (uint8_t)(rhPct * 2.0f);
        _buffer[_cursor++] = channel;
        _buffer[_cursor++] = LPP_RELATIVE_HUMIDITY;
        _buffer[_cursor++] = val;
        return true;
    }

    bool addAnalogInput(uint8_t channel, float value) {
        if (_cursor + 4 > _maxSize) return false;
        int16_t val = (int16_t)(value * 100.0f);
        _buffer[_cursor++] = channel;
        _buffer[_cursor++] = LPP_ANALOG_INPUT;
        _buffer[_cursor++] = (val >> 8) & 0xFF;
        _buffer[_cursor++] = val & 0xFF;
        return true;
    }

    bool addLuminosity(uint8_t channel, uint16_t lux) {
        if (_cursor + 4 > _maxSize) return false;
        _buffer[_cursor++] = channel;
        _buffer[_cursor++] = LPP_LUMINOSITY;
        _buffer[_cursor++] = (lux >> 8) & 0xFF;
        _buffer[_cursor++] = lux & 0xFF;
        return true;
    }

    bool addVoltage(uint8_t channel, float volts) {
        if (_cursor + 4 > _maxSize) return false;
        uint16_t val = (uint16_t)(volts * 100.0f);
        _buffer[_cursor++] = channel;
        _buffer[_cursor++] = LPP_VOLTAGE;
        _buffer[_cursor++] = (val >> 8) & 0xFF;
        _buffer[_cursor++] = val & 0xFF;
        return true;
    }
};

#endif // CAYENNE_LPP_ENCODER_H
