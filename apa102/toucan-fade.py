#!/usr/bin/env python3
import toucan_helpers as toucan
import time

try:
    lights = toucan.setup()
    for x in range(0,256):
        for y in range(0,8):
            print("setting " + str(y) + " to " + str(x))
            lights.set_pixel(y, x, x, x)
        lights.show() 

    toucan.lightsOut(lights)

except Exception as e:
    print(e)

finally:
    toucan.gpioClean()


