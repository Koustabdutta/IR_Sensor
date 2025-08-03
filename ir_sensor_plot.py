import streamlit as st
import serial
import pandas as pd
import time

# Set Streamlit page config
st.set_page_config(page_title="ESP32 IR Sensor Realtime Plot", layout="wide")

# Serial setup
SERIAL_PORT = '/dev/ttyUSB0'  # Replace with your actual port
BAUD_RATE = 115200

@st.cache_resource
def init_serial():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Allow ESP32 to reset
        return ser
    except Exception as e:
        st.error(f"Serial connection error: {e}")
        return None

ser = init_serial()

# Streamlit UI
st.title("📊 Real-time IR Sensor Plot (ESP32)")
plot_area = st.empty()

# Data buffer
data_buffer = pd.DataFrame(columns=["S1", "S2", "S3", "S4", "S5"])

# Live loop
if ser:
    while True:
        line = ser.readline().decode('utf-8').strip()
        try:
            values = list(map(int, line.split(',')))
            if len(values) == 5:
                new_row = pd.DataFrame([values], columns=["S1", "S2", "S3", "S4", "S5"])
                data_buffer = pd.concat([data_buffer, new_row], ignore_index=True)

                # Keep last 100 samples only
                if len(data_buffer) > 100:
                    data_buffer = data_buffer.iloc[-100:]

                # Plot
                plot_area.line_chart(data_buffer)
        except:
            continue
