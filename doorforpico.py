from machine import Pin
import time
TRIG = Pin(3, Pin.OUT)
ECHO = Pin(4, Pin.IN)
TRIGGER_DISTANCE = 30
RESET_DISTANCE = 45
def distance_cm():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    start = time.ticks_us()
    while ECHO.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > 30000:
            return -1
    start = time.ticks_us()
    while ECHO.value() == 1:
        if time.ticks_diff(time.ticks_us(), start) > 30000:
            return -1
    duration = time.ticks_diff(time.ticks_us(), start)
    return duration / 58
print("DOOR SYSTEM READY")
triggered = False
hits = 0
while True:
    d = distance_cm()
    if d > 0:
        print("Distance:", round(d, 1), "cm")
        if d < TRIGGER_DISTANCE and not triggered:
            hits += 1
            if hits >= 3:
                print("DOOR_OPEN")
                triggered = True
                hits = 0
        elif d >= TRIGGER_DISTANCE:
            hits = 0
        if d > RESET_DISTANCE:
            triggered = False
    time.sleep_ms(80)