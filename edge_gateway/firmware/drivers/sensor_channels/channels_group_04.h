#ifndef CHANNELS_GROUP_04_H
#define CHANNELS_GROUP_04_H

#include <stdint.h>
#include <math.h>

class IndustrialSensorChannel_061 {
private:
    uint8_t _channelId = 60;
    uint16_t _modbusRegisterBase = 1600;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_061(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_062 {
private:
    uint8_t _channelId = 61;
    uint16_t _modbusRegisterBase = 1610;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_062(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_063 {
private:
    uint8_t _channelId = 62;
    uint16_t _modbusRegisterBase = 1620;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_063(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_064 {
private:
    uint8_t _channelId = 63;
    uint16_t _modbusRegisterBase = 1630;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_064(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_065 {
private:
    uint8_t _channelId = 64;
    uint16_t _modbusRegisterBase = 1640;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_065(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_066 {
private:
    uint8_t _channelId = 65;
    uint16_t _modbusRegisterBase = 1650;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_066(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_067 {
private:
    uint8_t _channelId = 66;
    uint16_t _modbusRegisterBase = 1660;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_067(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_068 {
private:
    uint8_t _channelId = 67;
    uint16_t _modbusRegisterBase = 1670;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_068(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_069 {
private:
    uint8_t _channelId = 68;
    uint16_t _modbusRegisterBase = 1680;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_069(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_070 {
private:
    uint8_t _channelId = 69;
    uint16_t _modbusRegisterBase = 1690;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_070(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_071 {
private:
    uint8_t _channelId = 70;
    uint16_t _modbusRegisterBase = 1700;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_071(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_072 {
private:
    uint8_t _channelId = 71;
    uint16_t _modbusRegisterBase = 1710;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_072(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_073 {
private:
    uint8_t _channelId = 72;
    uint16_t _modbusRegisterBase = 1720;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_073(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_074 {
private:
    uint8_t _channelId = 73;
    uint16_t _modbusRegisterBase = 1730;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_074(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_075 {
private:
    uint8_t _channelId = 74;
    uint16_t _modbusRegisterBase = 1740;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_075(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_076 {
private:
    uint8_t _channelId = 75;
    uint16_t _modbusRegisterBase = 1750;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_076(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_077 {
private:
    uint8_t _channelId = 76;
    uint16_t _modbusRegisterBase = 1760;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_077(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_078 {
private:
    uint8_t _channelId = 77;
    uint16_t _modbusRegisterBase = 1770;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_078(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_079 {
private:
    uint8_t _channelId = 78;
    uint16_t _modbusRegisterBase = 1780;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_079(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_080 {
private:
    uint8_t _channelId = 79;
    uint16_t _modbusRegisterBase = 1790;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_080(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

#endif // CHANNELS_GROUP_04_H
