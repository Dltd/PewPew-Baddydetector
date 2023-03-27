#!/usr/bin/python
# Pi LED Loop Test v0.69
# -----------------------
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Version: v2
# -----------------------
import RPi.GPIO as GPIO
import time
import threading

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
#pins = [4, 17, 27, 23, 22, 18, 24, 25]
pins = [4, 17, 18, 22, 23, 24, 25, 27]
GPIO.setup(pins, GPIO.OUT)

# Define a function to blink a single LED
def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)

# Define a function to blink all LEDs
def blink_all():
    while True:
        for pin in pins:
            blink(pin)

# Start the blinking thread
blink_thread = threading.Thread(target=blink_all)
blink_thread.start()

# Loop until user types 'exit'
while True:
    # Prompt the user to type 'exit' to stop the loop
    print("Type 'exit' to stop the test.")
    user_input = input("> ")

    # If user types 'exit', break out of the loop and stop the blinking thread
    if user_input == 'exit':
        GPIO.cleanup()
        break
