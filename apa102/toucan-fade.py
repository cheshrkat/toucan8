#!/usr/bin/env python3
import toucan_helpers as toucan
import time

try:
    lights = toucan.setup()
    toucan.fadeUp(lights)
    toucan.fadeDown(lights)
    toucan.lightsOut(lights)

except Exception as e:
    print(e)

finally:
    toucan.gpioClean()
