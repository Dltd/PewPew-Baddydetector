#!/usr/bin/python
# BaddyDetector v0.69
# -----------------------
# pewclient.{version}.py PoC
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Version: v3
# -----------------------
# This PoC consists of a server and client script, the server listens to multiple ports,
# and the client connects to these ports. Log files are 'tailed' and will have the client
# blink a corresponding LED when the new entries arrive.
#
# The pewclient.py script starts by executing an LED pattern ( pewpew_engage() )
# The startup pattern can assist in finding a dead LED and also just looks fun to have as start indicator.
# ------------
# It is a Python client that connects to a remote server to receive log updates.
# It establishes multiple connections to the server on specified ports and listens for updates.
# ------------
# When data is received, the script toggles corresponding LEDs to indicate activity.
# The server script is pewserver.{version}.py.
# ------------
# You have to update the SERVER_IP to match the server you connect to.
# ------------
# This PoC was built on a Raspberry Pi 1
# and uses GPIO pins 4, 17, 18, 22, 23, 24, 25 and 27 to control the LEDs.
# -----------------------
#

# Import required libraries and set up global variables
import asyncio  # Import the asyncio library for creating asynchronous tasks
import aioconsole  # Import the aioconsole library for reading user input asynchronously
from gpiozero import LED  # Import the LED class from the gpiozero library for controlling LEDs
from asyncio import StreamReader, StreamWriter  # Import the StreamReader and StreamWriter classes for communicating with the server
import time  # Import the time library for adding delays in the code
import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling the Raspberry Pi's GPIO pins

SERVER_IP = "YOUR_SERVER_IP_HERE"  # Set the IP address of the server
START_PORT = 54631  # Set the starting port number for the program
NUM_PORTS = 8  # Set the number of ports to be used in the program
GPIO_PINS = [4, 17, 18, 22, 23, 24, 25, 27]  # Define a list of GPIO pins to be used for the LEDs
leds = [LED(pin) for pin in GPIO_PINS]  # Create a list of LED objects to be used in the program

# Define a function that moves the LEDs back and forth and blinks them in a specific pattern
def pewpew_engage():
    # Set up the GPIO pins
    pins = [4, 17, 18, 22, 23, 24, 25, 27]
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    # Move LEDs back and forth twice
    for j in range(2):
        for i in range(8):
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.07)
            GPIO.output(pins[i], GPIO.LOW)
        for i in range(6, 0, -1):
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(0.07)
            GPIO.output(pins[i], GPIO.LOW)

    # Turn all LEDs off
    for i in range(8):
        GPIO.output(pins[i], GPIO.LOW)

    # Blink LEDs 4 and 6
    for i in range(2):
        GPIO.output(pins[3], GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pins[3], GPIO.LOW)
        GPIO.output(pins[5], GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pins[5], GPIO.LOW)

    # Very shortly blink all LEDs
    for i in range(2):
        for i in range(8):
            GPIO.output(pins[i], GPIO.HIGH)
        time.sleep(0.05)
        for i in range(8):
            GPIO.output(pins[i], GPIO.LOW)


# Execute the function that moves the LEDs
pewpew_engage()

# Define an asynchronous function that connects to the server and reads data from the specified port.
# Asynchronous tasks in the asyncio module allow for concurrent execution of multiple tasks without
# blocking the main thread. The module uses an event loop to manage the execution of these tasks, 
# allowing them to run concurrently and switch between each other when waiting for input/output or sleeping.
async def handle_port(port: int, led: LED):
    async def blink_led():
        led.blink(on_time=0.05, off_time=0.05, n=1)
        await asyncio.sleep(0.2)

    while True:
        try:
            reader, writer = await asyncio.open_connection(SERVER_IP, port)
            while True:
                data = await reader.read(1)
                if data:
                    await blink_led()
                else:
                    data == b'0'
        except ConnectionError:
            print(f"Connection to port {port} failed. Retrying in 5 seconds...")
            await asyncio.sleep(5)
        except asyncio.CancelledError:
            print(f"Disconnecting from port {port}...")
            writer.close()
            await writer.wait_closed()
            break

# Define an asynchronous function that reads user input and stops the program when the user types "exit"
async def user_input():
    while True:
        user_command = await aioconsole.ainput("Type 'exit' to stop the program: ")
        if user_command.lower() == "exit":
            return

# Define the main function that creates tasks for each port and user input, and runs the tasks
async def main():
    tasks = [asyncio.create_task(handle_port(START_PORT + i, leds[i])) for i in range(NUM_PORTS)]
    input_task = asyncio.create_task(user_input())

    try:
        await input_task
    except KeyboardInterrupt:
        pass
    finally:
        print("\nDisconnecting from the server...")
        for task in tasks:
            task.cancel()
            await task

# Execute the main function
if __name__ == "__main__":
    asyncio.run(main())  # Run the main function using asyncio's run() function
