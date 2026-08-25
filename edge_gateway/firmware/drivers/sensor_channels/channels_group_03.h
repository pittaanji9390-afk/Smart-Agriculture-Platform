#ifndef CHANNELS_GROUP_03_H
#define CHANNELS_GROUP_03_H

#include <stdint.h>
#include <math.h>

class IndustrialSensorChannel_041 {
private:
    uint8_t _channelId = 40;
    uint16_t _modbusRegisterBase = 1400;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_041(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_042 {
private:
    uint8_t _channelId = 41;
    uint16_t _modbusRegisterBase = 1410;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_042(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_043 {
private:
    uint8_t _channelId = 42;
    uint16_t _modbusRegisterBase = 1420;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_043(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_044 {
private:
    uint8_t _channelId = 43;
    uint16_t _modbusRegisterBase = 1430;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_044(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_045 {
private:
    uint8_t _channelId = 44;
    uint16_t _modbusRegisterBase = 1440;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_045(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_046 {
private:
    uint8_t _channelId = 45;
    uint16_t _modbusRegisterBase = 1450;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_046(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_047 {
private:
    uint8_t _channelId = 46;
    uint16_t _modbusRegisterBase = 1460;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_047(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_048 {
private:
    uint8_t _channelId = 47;
    uint16_t _modbusRegisterBase = 1470;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_048(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_049 {
private:
    uint8_t _channelId = 48;
    uint16_t _modbusRegisterBase = 1480;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_049(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_050 {
private:
    uint8_t _channelId = 49;
    uint16_t _modbusRegisterBase = 1490;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_050(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_051 {
private:
    uint8_t _channelId = 50;
    uint16_t _modbusRegisterBase = 1500;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_051(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_052 {
private:
    uint8_t _channelId = 51;
    uint16_t _modbusRegisterBase = 1510;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_052(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_053 {
private:
    uint8_t _channelId = 52;
    uint16_t _modbusRegisterBase = 1520;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_053(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_054 {
private:
    uint8_t _channelId = 53;
    uint16_t _modbusRegisterBase = 1530;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_054(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_055 {
private:
    uint8_t _channelId = 54;
    uint16_t _modbusRegisterBase = 1540;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_055(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_056 {
private:
    uint8_t _channelId = 55;
    uint16_t _modbusRegisterBase = 1550;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_056(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_057 {
private:
    uint8_t _channelId = 56;
    uint16_t _modbusRegisterBase = 1560;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_057(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_058 {
private:
    uint8_t _channelId = 57;
    uint16_t _modbusRegisterBase = 1570;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_058(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_059 {
private:
    uint8_t _channelId = 58;
    uint16_t _modbusRegisterBase = 1580;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_059(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_060 {
private:
    uint8_t _channelId = 59;
    uint16_t _modbusRegisterBase = 1590;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_060(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

#endif // CHANNELS_GROUP_03_H
