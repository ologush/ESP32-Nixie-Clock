print("Hello World")

import board
import digitalio
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    led.fill((255, 0, 0))
    time.sleep(0.5)
    led.fill((0, 255, 0))
    time.sleep(0.5)
    led.fill((0, 0, 255))
    time.sleep(0.5)
    print("test")
