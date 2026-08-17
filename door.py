import serial
import time
import pyautogui

# Change this if your Pico is on another COM port
PORT = "COM4"
BAUD = 115200
print("Connecting to Pico...")
pico = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)
print("================================")
print(" DOOR DESKTOP SWITCHER READY")
print("================================")
print("Open the door to switch desktop.")
while True:
    line = pico.readline().decode("utf-8", errors="ignore").strip()
    if line:
        print(line)
    if line == "DOOR_OPEN":
        print("door open")
        print("switching desktop...")
        pyautogui.hotkey("ctrl", "win", "right")