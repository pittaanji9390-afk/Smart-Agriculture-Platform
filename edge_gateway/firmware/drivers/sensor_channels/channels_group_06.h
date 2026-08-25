#ifndef CHANNELS_GROUP_06_H
#define CHANNELS_GROUP_06_H

#include <stdint.h>
#include <math.h>

class IndustrialSensorChannel_101 {
private:
    uint8_t _channelId = 100;
    uint16_t _modbusRegisterBase = 2000;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_101(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_102 {
private:
    uint8_t _channelId = 101;
    uint16_t _modbusRegisterBase = 2010;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_102(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_103 {
private:
    uint8_t _channelId = 102;
    uint16_t _modbusRegisterBase = 2020;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_103(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_104 {
private:
    uint8_t _channelId = 103;
    uint16_t _modbusRegisterBase = 2030;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_104(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_105 {
private:
    uint8_t _channelId = 104;
    uint16_t _modbusRegisterBase = 2040;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_105(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_106 {
private:
    uint8_t _channelId = 105;
    uint16_t _modbusRegisterBase = 2050;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_106(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_107 {
private:
    uint8_t _channelId = 106;
    uint16_t _modbusRegisterBase = 2060;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_107(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_108 {
private:
    uint8_t _channelId = 107;
    uint16_t _modbusRegisterBase = 2070;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_108(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_109 {
private:
    uint8_t _channelId = 108;
    uint16_t _modbusRegisterBase = 2080;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_109(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_110 {
private:
    uint8_t _channelId = 109;
    uint16_t _modbusRegisterBase = 2090;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_110(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_111 {
private:
    uint8_t _channelId = 110;
    uint16_t _modbusRegisterBase = 2100;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_111(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_112 {
private:
    uint8_t _channelId = 111;
    uint16_t _modbusRegisterBase = 2110;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_112(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_113 {
private:
    uint8_t _channelId = 112;
    uint16_t _modbusRegisterBase = 2120;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_113(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_114 {
private:
    uint8_t _channelId = 113;
    uint16_t _modbusRegisterBase = 2130;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_114(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_115 {
private:
    uint8_t _channelId = 114;
    uint16_t _modbusRegisterBase = 2140;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_115(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_116 {
private:
    uint8_t _channelId = 115;
    uint16_t _modbusRegisterBase = 2150;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_116(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_117 {
private:
    uint8_t _channelId = 116;
    uint16_t _modbusRegisterBase = 2160;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_117(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_118 {
private:
    uint8_t _channelId = 117;
    uint16_t _modbusRegisterBase = 2170;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_118(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_119 {
private:
    uint8_t _channelId = 118;
    uint16_t _modbusRegisterBase = 2180;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_119(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_120 {
private:
    uint8_t _channelId = 119;
    uint16_t _modbusRegisterBase = 2190;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_120(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

#endif // CHANNELS_GROUP_06_H
