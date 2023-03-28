#!/usr/bin/python
# Pi multiple LED tests v0.69
# -----------------------
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Version: v1
# -----------------------
import RPi.GPIO as GPIO
import time
import threading

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
pins = [4, 17, 18, 22, 23, 24, 25, 27]
GPIO.setup(pins, GPIO.OUT)

# Map the pin numbers to LED numbers
leds = {}
for i, pin in enumerate(pins):
    leds[i + 1] = pin

# Initialize loop thread to None
loop_thread = None

# Define a function to turn an LED on or off
def toggle_led(led_num, state):
    if state == "on":
        GPIO.output(leds[led_num], GPIO.HIGH)
    elif state == "off":
        GPIO.output(leds[led_num], GPIO.LOW)

# Define a function to blink all LEDs in sequence
def loop_test():
    while not stop_loop_test.is_set():
        for led_num in range(1, 9):
            toggle_led(led_num, "on")
            time.sleep(0.1)
            toggle_led(led_num, "off")
        time.sleep(0.5)

# Define a function to print a boxed message
def print_boxed_message(message):
    print("-" * (len(message) + 4))
    print("| " + message + " |")
    print("-" * (len(message) + 4))

# Print the help message
print_boxed_message("Available commands:")
print("  'led <num> on': turn a specific LED on")
print("  'led <num> off': turn a specific LED off")
print("  'all leds on': turn all LEDs on")
print("  'all leds off': turn all LEDs off")
print("  'start loop test': start blinking all LEDs in sequence")
print("  'stop loop test': stop blinking all LEDs in sequence")
print("  'help': display this message")
print("  'exit': quit the program")
print("-" * 24)

# Create a flag to stop the loop test
stop_loop_test = threading.Event()

# Loop until user types 'exit'
try:
    while True:
        # Prompt the user to enter an LED command or exit
        print("Enter a command ('help' for available commands) or 'exit' to quit.")
        user_input = input("> ")

        # Parse the user input
        try:
            if user_input == "help":
                print_boxed_message("Available commands:")
                print("  'led <num> on': turn a specific LED on")
                print("  'led <num> off': turn a specific LED off")
                print("  'all leds on': turn all LEDs on")
                print("  'all leds off': turn all LEDs off")
                print("  'start loop test': start blinking all LEDs in sequence")
                print("  'stop loop test': stop blinking all LEDs in sequence")
                print("  'help': display this message")
                print("  'exit': quit the program")
                print("-" * 24)
                continue
            elif user_input == "start loop test":
                stop_loop_test.clear()
                loop_thread = threading.Thread(target=loop_test)
                loop_thread.start()
                continue
            elif user_input == "stop loop test":
                stop_loop_test.set()
                continue
            elif user_input == "all leds on":
                for pin in pins:
                    GPIO.output(pin, GPIO.HIGH)
                continue
            elif user_input == "all leds off":
                for pin in pins:
                    GPIO.output(pin, GPIO.LOW)
                continue
            else:
                command, led_num, state = user_input.split()
                led_num = int(led_num)
                if led_num not in leds:
                    raise ValueError("Invalid LED number.")
                if state not in ("on", "off"):
                    raise ValueError("Invalid LED state.")
        except (ValueError, TypeError):
            if user_input == "exit":
                stop_loop_test.set()
                break
            else:
                print("Invalid input. Try again.")
                continue

        # Turn the LED on or off
        toggle_led(led_num, state)

        # If loop test is running, return to prompt without delay
        if loop_thread and loop_thread.is_alive():
            continue

        # Prompt the user to enter another command
        print("Enter another command or 'exit' to quit.")
finally:
    GPIO.cleanup()
