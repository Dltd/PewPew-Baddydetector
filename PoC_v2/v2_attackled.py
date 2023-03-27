#!/usr/bin/python
# BaddyDetector v0.69
# -----------------------
# attackled PoC using pewpewclient.sh
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# each LED has its own script as quick and dirty PoC
# client to connect to a tcp port
import socket
import sys
from gpiozero import LED
from time import sleep


TCP_IP = 'YOUR_SERVER_IP_HERE'
TCP_PORT = 54631

#     pins 27, 22, 23, 24 and 25 are used for leds 1-5
# Rpi 1 pins:  4, 17, 27, 23, 22, 18, 24, 25
# This one will blink the LED connected to GPIO 4
led = LED(4)

# connect and keep waiting for data.
# when data is received, blink the led shortly
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
  line = s.recv(1024)
  if line:
#    print(line)
#blinking with gpiozero library
    led.on()
    sleep(0.05)
    led.off()
    sleep(0.05)
  else:
    break

s.close()
