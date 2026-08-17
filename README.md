ok so to use this first you have to stick the breadboard to the door frame horizontally and connect the pi to your computer
if you have a w series pi then no need for the wire.
REQUIREMENTS:
breadboard (obviously)
rasberry pico pi 1/2/1W/2W
ultrasonic sensor HC-SR04
4 jumper wires
2 resistors any but i used 470ohm
a cable to connect to pc or if W then no need
FOR THE WIRING:
HC-SR04	
Connect to VCC	VBUS 
GND	to any Pico GND
TRIG to GP3
ECHO to resistor divider → GP4
## 🔌 Wiring Diagram

### Raspberry Pi Pico 2 + HC-SR04

```text
                         HC-SR04
                    ┌───────────────┐
                    │               │
                    │ VCC TRIG ECHO GND
                    └─┬───┬────┬───┬┘
                      │   │    │   │
                      │   │    │   └───────────────┐
                      │   │    │                   │
                      │   │   [480Ω]               │
                      │   │    │                   │
                      │   │    ●──────── GP4       │
                      │   │    │                   │
                      │   │   [480Ω]               │
                      │   │    │                   │
                      │   │    └───────────────────┤
                      │   │                        │
                      │   └──────────── GP3        │
                      │                            │
                      └──────────────── VBUS       │
                                                   │
                                                   │
                    Raspberry Pi Pico 2           │
                  ┌──────────────────────┐         │
                  │                      │         │
                  │ VBUS  ───────────────┘         │
                  │ GP3   ───── TRIG               │
                  │ GP4   ───── ECHO divider       │
                  │ GND   ────────────────┐        │
                  │                      ││        │
                  └──────────────────────┘│        │
                                         ││        │
                                         └─────────┘
              and now go to thonny or any other program to use the code for rasberry pi pico and paste the doorforpico.py code and run it.
              make sure it shows distance like:
              DOOR SYSTEM READY
              Distance: 57.1 cm
              Distance: 56.9 cm
              Distance: 56.9 cm
              Distance: 56.9 cm
              Distance: 57.1 cm
              Distance: 57.0 cm
              Distance: 57.1 cm
              Distance: 57.0 cm
              Distance: 56.9 cm
              Distance: 57.1 cm
              Distance: 57.0 cm
              Distance: 57.0 cm
              Distance: 57.0 cm
              Distance: 57.0 cm
              Distance: 57.0 cm
              Distance: 57.1 cm
              Distance: 57.0 cm
              Distance: 57.1 cm
              Distance: 57.0 cm
              Distance: 56.9 cm
              Distance: 56.9 cm
              Distance: 56.9 cm
              Distance: 57.1 cm
              unless it prints this output, you might have done something wrong.
              it took some time to get the resistors right make sure you connect the resistor as the HCSR04 can output 5v which may be dangerous for the pi.
              after this, go and make a new python file and paste the contents of door.py and run it. you might get some errors.
              TO FIX THEM:
              first make sure you have python 3.13 installed
              make sure you have pyautogui installed if not, RUN:
              py -m pip install pyautogui
              after this the program should run properly.
              now that everything is set up, make a new dekstop 2 and go back to dekstop 1.
              you should see that the dekstop changes on opening the door.
              you might need to change the distance where the pico code says door opened so change the line(s):
              TRIGGER_DISTANCE = 30
              RESET_DISTANCE = 45
              hope this works for you
