import board
import digitalio
import time
import neopixel

import os
import ipaddress
import wifi
import socketpool


led = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Creating AP")

wifi.radio.start_ap(ssid=os.getenv('CIRCUITPY_AP_SSID'), password=os.getenv('CIRCUITPY_AP_PASSWORD'))

while True:
    led.fill((255, 0, 0))
    time.sleep(0.5)
    led.fill((0, 255, 0))
    time.sleep(0.5)
    led.fill((0, 0, 255))
    time.sleep(0.5)
