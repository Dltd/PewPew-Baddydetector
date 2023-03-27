#!/usr/bin/python
# client to connect to a tcp port
import socket
import sys
from gpiozero import LED
from time import sleep

TCP_IP = 'YOUR_SERVER_IP_HERE'
TCP_PORT = 54632

#     pins 27, 22, 23, 24 and 25 are used for leds 1-5
led = LED(27)

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
