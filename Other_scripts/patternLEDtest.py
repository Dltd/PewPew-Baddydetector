#!/usr/bin/python
# Pi LED pattern test v0.69
# -----------------------
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Version: v1
# -----------------------
import RPi.GPIO as GPIO
import time
import itertools

# Set the pin numbering mode
GPIO.setmode(GPIO.BCM)

# Define the pins for the LEDs
pins = [4, 17, 18, 22, 23, 24, 25, 27]

# Set up the GPIO pins for output
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Define the patterns for the LEDs
patterns = [
    [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 0],
    ],
    # Next pattern here...
    [
        [0, 1, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
    ],
    [
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
    ],
    # Next pattern here...
    [
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
    ],
    [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
    ],
    # Next pattern here...
    [
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    # Next pattern here...
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
]

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Loop through the patterns
while True:
    for pattern in patterns:
        for row in pattern:
            for i in range(8):
                if row[i]:
                    GPIO.output(pins[i], GPIO.HIGH)
                else:
                    GPIO.output(pins[i], GPIO.LOW)
            time.sleep(0.1)
# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Loop through the patterns
while True:
    for pattern in patterns:
        for row in pattern:
            for i in range(8):
                if row[i]:
                    GPIO.output(pins[i], GPIO.HIGH)
                else:
                    GPIO.output(pins[i], GPIO.LOW)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)
# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Loop through the patterns
while True:
    for pattern in patterns:
        for row in pattern:
            for i in range(8):
                if row[i]:
                    GPIO.output(pins[i], GPIO.HIGH)
                else:
                    GPIO.output(pins[i], GPIO.LOW)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            if i % 2 == 0:
                GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            if i % 2 == 1:
                GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)
# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Loop through the patterns
while True:
    for pattern in patterns:
        for row in pattern:
            for i in range(8):
                if row[i]:
                    GPIO.output(pins[i], GPIO.HIGH)
                else:
                    GPIO.output(pins[i], GPIO.LOW)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            GPIO.output(pins[i - 1], GPIO.HIGH)
            GPIO.output(pins[7 - i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            if i % 2 == 0:
                GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)
            if i % 2 == 1:
                GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.1)

        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)

    # Cleanup
    GPIO.cleanup()
