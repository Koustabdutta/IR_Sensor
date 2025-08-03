# 📊 Real-Time Sensor Data Plotting using ESP32 and Python

This project enables real-time data visualization from an ESP32 microcontroller using a Python-based plotting interface. The ESP32 reads sensor data (e.g., PIR, temperature, pressure) and streams it over USB serial to a Python script that dynamically plots the incoming data.

---

## 🚀 Features

- 📟 Real-time data acquisition via Serial (USB)
- 📈 Live plotting using `matplotlib` with Python
- 🔌 Cross-platform (tested on Linux, should work on Windows/Mac)
- 🧠 Ready to integrate with anomaly detection or ML models

---

## 🧰 Requirements

### Microcontroller:
- ESP32 (or compatible board)
- Sensor (PIR / temperature / pressure / custom)

### Host PC:
- Python 3.x
- Required libraries:
  ```bash
  pip install pyserial matplotlib
