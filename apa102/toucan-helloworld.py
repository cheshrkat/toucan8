#!/usr/bin/env python3
from apa102 import APA102
import RPi.GPIO as GPIO
import time

# Use try/catch/finally to ensure the GPIO always gets cleaned up.
try:
    print("Toucan: hello world! Note LED brightness is turned down to 0.1. This example uses the APA102 API directly, without any helpers.")
    # Initialise lights with APA210
    lights = APA102(8, 23, 24, brightness=0.1)

    print("Toucan: setting pixels to rainbow.")
    # ROYGBIV plus OG pride pink to make up 8
    lights.set_pixel(0, 97, 45, 71)
    lights.set_pixel(1, 255, 0, 0)
    lights.set_pixel(2, 255, 165, 0)
    lights.set_pixel(3, 255, 255, 0)
    lights.set_pixel(4, 0, 128, 0)
    lights.set_pixel(5, 0, 0, 255)
    lights.set_pixel(6, 75, 0, 130)
    lights.set_pixel(7, 238, 130, 238)

    print("Toucan: calling show() to update the Toucan with the pixels we just set")
    lights.show()

    print("Toucan: a little pause to admire...")
    time.sleep(1)

    print("Toucan: now turning them all off again")
    lights.set_pixel(0, 0, 0, 0)
    lights.set_pixel(1, 0, 0, 0)
    lights.set_pixel(2, 0, 0, 0)
    lights.set_pixel(3, 0, 0, 0)
    lights.set_pixel(4, 0, 0, 0)
    lights.set_pixel(5, 0, 0, 0)
    lights.set_pixel(6, 0, 0, 0)
    lights.set_pixel(7, 0, 0, 0)
    lights.show()
    
except Exception as e: 
    print("Toucan: well we certainly hoped we wouldn't up here, but something has gone wrong.")
    print(e)

finally:
    print("Toucan: cleaning up GPIO")
    GPIO.cleanup()
    print("Toucan: done!")
