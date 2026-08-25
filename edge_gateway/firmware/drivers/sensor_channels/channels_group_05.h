#ifndef CHANNELS_GROUP_05_H
#define CHANNELS_GROUP_05_H

#include <stdint.h>
#include <math.h>

class IndustrialSensorChannel_081 {
private:
    uint8_t _channelId = 80;
    uint16_t _modbusRegisterBase = 1800;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_081(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_082 {
private:
    uint8_t _channelId = 81;
    uint16_t _modbusRegisterBase = 1810;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_082(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_083 {
private:
    uint8_t _channelId = 82;
    uint16_t _modbusRegisterBase = 1820;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_083(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_084 {
private:
    uint8_t _channelId = 83;
    uint16_t _modbusRegisterBase = 1830;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_084(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_085 {
private:
    uint8_t _channelId = 84;
    uint16_t _modbusRegisterBase = 1840;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_085(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_086 {
private:
    uint8_t _channelId = 85;
    uint16_t _modbusRegisterBase = 1850;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_086(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_087 {
private:
    uint8_t _channelId = 86;
    uint16_t _modbusRegisterBase = 1860;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_087(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_088 {
private:
    uint8_t _channelId = 87;
    uint16_t _modbusRegisterBase = 1870;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_088(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_089 {
private:
    uint8_t _channelId = 88;
    uint16_t _modbusRegisterBase = 1880;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_089(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_090 {
private:
    uint8_t _channelId = 89;
    uint16_t _modbusRegisterBase = 1890;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_090(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_091 {
private:
    uint8_t _channelId = 90;
    uint16_t _modbusRegisterBase = 1900;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_091(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_092 {
private:
    uint8_t _channelId = 91;
    uint16_t _modbusRegisterBase = 1910;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_092(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_093 {
private:
    uint8_t _channelId = 92;
    uint16_t _modbusRegisterBase = 1920;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_093(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_094 {
private:
    uint8_t _channelId = 93;
    uint16_t _modbusRegisterBase = 1930;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_094(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_095 {
private:
    uint8_t _channelId = 94;
    uint16_t _modbusRegisterBase = 1940;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_095(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_096 {
private:
    uint8_t _channelId = 95;
    uint16_t _modbusRegisterBase = 1950;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_096(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_097 {
private:
    uint8_t _channelId = 96;
    uint16_t _modbusRegisterBase = 1960;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_097(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_098 {
private:
    uint8_t _channelId = 97;
    uint16_t _modbusRegisterBase = 1970;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_098(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_099 {
private:
    uint8_t _channelId = 98;
    uint16_t _modbusRegisterBase = 1980;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_099(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

class IndustrialSensorChannel_100 {
private:
    uint8_t _channelId = 99;
    uint16_t _modbusRegisterBase = 1990;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_100(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
    void setCalibration(float slope, float intercept) {
        _calibrationSlope = slope;
        _calibrationIntercept = intercept;
    }
    float readCalibratedValue(float rawAnalogADC) {
        float calibrated = (rawAnalogADC * _calibrationSlope) + _calibrationIntercept;
        _runningSum += calibrated;
        _sampleCount++;
        return calibrated;
    }
    float getRunningAverage() const {
        return _sampleCount > 0 ? (_runningSum / (float)_sampleCount) : 0.0f;
    }
    void resetAccumulator() {
        _sampleCount = 0;
        _runningSum = 0.0f;
    }
};

#endif // CHANNELS_GROUP_05_H
