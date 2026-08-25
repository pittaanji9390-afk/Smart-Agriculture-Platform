#ifndef CHANNELS_GROUP_01_H
#define CHANNELS_GROUP_01_H

#include <stdint.h>
#include <math.h>

class IndustrialSensorChannel_001 {
private:
    uint8_t _channelId = 0;
    uint16_t _modbusRegisterBase = 1000;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_001(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_002 {
private:
    uint8_t _channelId = 1;
    uint16_t _modbusRegisterBase = 1010;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_002(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_003 {
private:
    uint8_t _channelId = 2;
    uint16_t _modbusRegisterBase = 1020;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_003(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_004 {
private:
    uint8_t _channelId = 3;
    uint16_t _modbusRegisterBase = 1030;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_004(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_005 {
private:
    uint8_t _channelId = 4;
    uint16_t _modbusRegisterBase = 1040;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_005(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_006 {
private:
    uint8_t _channelId = 5;
    uint16_t _modbusRegisterBase = 1050;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_006(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_007 {
private:
    uint8_t _channelId = 6;
    uint16_t _modbusRegisterBase = 1060;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_007(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_008 {
private:
    uint8_t _channelId = 7;
    uint16_t _modbusRegisterBase = 1070;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_008(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_009 {
private:
    uint8_t _channelId = 8;
    uint16_t _modbusRegisterBase = 1080;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_009(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_010 {
private:
    uint8_t _channelId = 9;
    uint16_t _modbusRegisterBase = 1090;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_010(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_011 {
private:
    uint8_t _channelId = 10;
    uint16_t _modbusRegisterBase = 1100;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_011(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_012 {
private:
    uint8_t _channelId = 11;
    uint16_t _modbusRegisterBase = 1110;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_012(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_013 {
private:
    uint8_t _channelId = 12;
    uint16_t _modbusRegisterBase = 1120;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_013(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_014 {
private:
    uint8_t _channelId = 13;
    uint16_t _modbusRegisterBase = 1130;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_014(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_015 {
private:
    uint8_t _channelId = 14;
    uint16_t _modbusRegisterBase = 1140;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_015(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_016 {
private:
    uint8_t _channelId = 15;
    uint16_t _modbusRegisterBase = 1150;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_016(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_017 {
private:
    uint8_t _channelId = 16;
    uint16_t _modbusRegisterBase = 1160;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_017(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_018 {
private:
    uint8_t _channelId = 17;
    uint16_t _modbusRegisterBase = 1170;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_018(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_019 {
private:
    uint8_t _channelId = 18;
    uint16_t _modbusRegisterBase = 1180;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_019(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

class IndustrialSensorChannel_020 {
private:
    uint8_t _channelId = 19;
    uint16_t _modbusRegisterBase = 1190;
    float _calibrationSlope = 1.0f;
    float _calibrationIntercept = 0.0f;
    uint32_t _sampleCount = 0;
    float _runningSum = 0.0f;
public:
    IndustrialSensorChannel_020(float slope = 1.0f, float intercept = 0.0f) : _calibrationSlope(slope), _calibrationIntercept(intercept) {}
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

#endif // CHANNELS_GROUP_01_H
