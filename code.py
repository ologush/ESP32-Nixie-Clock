import board
import digitalio
import time
import neopixel

import os
import ipaddress
import wifi
import socketpool

from adafruit_httpserver import Server, Request, Response

print("Creating AP")

wifi.radio.start_ap(ssid=os.getenv('CIRCUITPY_AP_SSID'), password=os.getenv('CIRCUITPY_AP_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool)
print(wifi.radio.ipv4_address_ap)
@server.route("/")
def base(request: Request):
    print("request received")

server.serve_forever(str(wifi.radio.ipv4_address_ap), 5000)
