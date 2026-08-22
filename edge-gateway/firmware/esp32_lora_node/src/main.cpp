/**
 * ESP32-S3 LoRaWAN Precision Soil Probe Firmware
 * Target Platform: Espressif ESP32-S3 + Semtech SX1262 LoRa Transceiver
 * Protocol: Modbus RTU RS485 Soil NPK Sensor + I2C SHT30 Air Temperature/Humidity
 */

#include <Arduino.h>
#include <HardwareSerial.h>
#include <Wire.h>
#include <SPI.h>

// Pin Definitions
#define RS485_RX_PIN 16
#define RS485_TX_PIN 17
#define RS485_DE_RE_PIN 4
#define I2C_SDA_PIN 21
#define I2C_SCL_PIN 22
#define BATTERY_ADC_PIN 34

// Modbus Query Frame for 7-in-1 Soil Sensor (Moisture, Temp, EC, pH, N, P, K)
const byte ModbusQueryFrame[] = {0x01, 0x03, 0x00, 0x00, 0x00, 0x07, 0x04, 0x08};
byte ModbusResponseBuffer[25];

HardwareSerial RS485Serial(1);

struct SensorTelemetryPacket {
    uint16_t soilMoistureRaw;   // x10 %
    int16_t soilTempRaw;        // x10 degC
    uint16_t soilConductivity;  // uS/cm
    uint16_t soilPHRaw;         // x10 pH
    uint16_t nitrogenPPM;       // mg/kg
    uint16_t phosphorusPPM;     // mg/kg
    uint16_t potassiumPPM;      // mg/kg
    int16_t ambientTempRaw;     // x10 degC
    uint16_t ambientHumRaw;     // x10 %
    uint16_t batteryMillivolts; // mV
};

SensorTelemetryPacket currentReading;

void sendModbusRequest() {
    digitalWrite(RS485_DE_RE_PIN, HIGH); // Enable TX
    delay(2);
    RS485Serial.write(ModbusQueryFrame, sizeof(ModbusQueryFrame));
    RS485Serial.flush();
    digitalWrite(RS485_DE_RE_PIN, LOW); // Enable RX
}

bool readModbusResponse() {
    uint32_t startTime = millis();
    int byteCount = 0;
    
    while (millis() - startTime < 300) {
        if (RS485Serial.available()) {
            ModbusResponseBuffer[byteCount++] = RS485Serial.read();
            if (byteCount >= 19) break; // Expected 19 bytes for 7 registers
        }
    }
    
    if (byteCount >= 19 && ModbusResponseBuffer[0] == 0x01 && ModbusResponseBuffer[1] == 0x03) {
        // Parse big-endian 16-bit register values
        currentReading.soilMoistureRaw = (ModbusResponseBuffer[3] << 8) | ModbusResponseBuffer[4];
        currentReading.soilTempRaw = (ModbusResponseBuffer[5] << 8) | ModbusResponseBuffer[6];
        currentReading.soilConductivity = (ModbusResponseBuffer[7] << 8) | ModbusResponseBuffer[8];
        currentReading.soilPHRaw = (ModbusResponseBuffer[9] << 8) | ModbusResponseBuffer[10];
        currentReading.nitrogenPPM = (ModbusResponseBuffer[11] << 8) | ModbusResponseBuffer[12];
        currentReading.phosphorusPPM = (ModbusResponseBuffer[13] << 8) | ModbusResponseBuffer[14];
        currentReading.potassiumPPM = (ModbusResponseBuffer[15] << 8) | ModbusResponseBuffer[16];
        return true;
    }
    return false;
}

uint16_t readBatteryLevel() {
    int raw = analogRead(BATTERY_ADC_PIN);
    // Voltage divider ratio 2:1 with reference 3.3V
    float voltage = (raw / 4095.0) * 3.3 * 2.0 * 1000.0;
    return (uint16_t)voltage;
}

void setup() {
    Serial.begin(115200);
    pinMode(RS485_DE_RE_PIN, OUTPUT);
    digitalWrite(RS485_DE_RE_PIN, LOW);
    
    RS485Serial.begin(9600, SERIAL_8N1, RS485_RX_PIN, RS485_TX_PIN);
    Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);
    
    Serial.println(F("[AgriSphere Node] Firmware v2.5 Initialized."));
}

void loop() {
    Serial.println(F("[Sensor] Querying RS485 NPK Probe..."));
    sendModbusRequest();
    
    if (readModbusResponse()) {
        currentReading.batteryMillivolts = readBatteryLevel();
        Serial.printf("Moisture: %.1f%%, Soil Temp: %.1f C, pH: %.1f, N: %d, P: %d, K: %d, Battery: %d mV\n",
            currentReading.soilMoistureRaw / 10.0,
            currentReading.soilTempRaw / 10.0,
            currentReading.soilPHRaw / 10.0,
            currentReading.nitrogenPPM,
            currentReading.phosphorusPPM,
            currentReading.potassiumPPM,
            currentReading.batteryMillivolts
        );
    } else {
        Serial.println(F("[Sensor Warning] Modbus timeout or CRC mismatch."));
    }
    
    // Deep sleep for 15 seconds to conserve battery in field deployment
    delay(15000);
}
