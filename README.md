# 🔥 ESP32 IR Sensor Array – Real-Time Plotting with Streamlit

This project demonstrates **real-time plotting** of a 5-channel **IR sensor array** (like Distronix or QTR-type) connected to an **ESP32**, with visualizations built using **Python and Streamlit**.

It’s ideal for projects like:
- Line-following robots
- Obstacle detection systems
- Edge tracking
- Smart sensing platforms

---

## ⚙️ Hardware Setup

### 🧩 Components Used
- ESP32 development board
- IR Sensor Array Module (5-channel)
- USB cable
- Jumper wires

### 🔌 Connections

| IR Sensor | ESP32 GPIO |
|-----------|-------------|
| Sensor 1  | GPIO32      |
| Sensor 2  | GPIO33      |
| Sensor 3  | GPIO25      |
| Sensor 4  | GPIO26      |
| Sensor 5  | GPIO27      |
| VCC       | 3.3V / 5V   |
| GND       | GND         |

> ⚠️ If using a 5V sensor with a 3.3V ESP32, use voltage dividers or logic-level converters.

---

## 💻 Software Overview

### 📜 Arduino Sketch

```cpp
#define S1 32
#define S2 33
#define S3 25
#define S4 26
#define S5 27

void setup() {
  Serial.begin(115200);
  pinMode(S1, INPUT);
  pinMode(S2, INPUT);
  pinMode(S3, INPUT);
  pinMode(S4, INPUT);
  pinMode(S5, INPUT);
}

void loop() {
  int v1 = digitalRead(S1);
  int v2 = digitalRead(S2);
  int v3 = digitalRead(S3);
  int v4 = digitalRead(S4);
  int v5 = digitalRead(S5);

  Serial.print(v1); Serial.print(",");
  Serial.print(v2); Serial.print(",");
  Serial.print(v3); Serial.print(",");
  Serial.print(v4); Serial.print(",");
  Serial.println(v5);

  delay(100);
}
