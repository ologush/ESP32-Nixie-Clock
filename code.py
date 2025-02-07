import board
import digitalio
import time
import neopixel

import os
import ipaddress
import wifi
import socketpool


led = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Connecting to WiFi")

wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Successfully connected to:" + " " + os.getenv('CIRCUITPY_WIFI_SSID'))

pool = socketpool.SocketPool(wifi.radio)

print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

print("My IP address is", wifi.radio.ipv4_address)

while True:
    led.fill((255, 0, 0))
    time.sleep(0.5)
    led.fill((0, 255, 0))
    time.sleep(0.5)
    led.fill((0, 0, 255))
    time.sleep(0.5)
