#!/usr/bin/env python3
import toucan_helpers as toucan
import time

print("toucan.py")

try:
    lights = toucan.setup()

    lights.set_pixel(0, 255, 0, 0)
    lights.set_pixel(1, 255, 165, 0)
    lights.set_pixel(2, 255, 255, 0)
    lights.set_pixel(3, 0, 128, 0)
    lights.set_pixel(4, 0, 0, 255)
    lights.set_pixel(5, 75, 0, 130)
    lights.set_pixel(6, 238, 130, 238)
    lights.set_pixel(7, 255, 255, 255)
    lights.show()
    time.sleep(1)

    toucan.fillUp(lights, 0, 255, 0)
    toucan.fillDown(lights, 0, 255, 255)
    toucan.fillRandom(lights)
    time.sleep(1)

    toucan.fadeUp(lights)
    toucan.fadeDown(lights)

except Exception as e: 
    print(e)

finally:
    toucan.lightsOut(lights)
    toucan.gpioClean()
