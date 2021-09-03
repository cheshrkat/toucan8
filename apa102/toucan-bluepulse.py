#!/usr/bin/env python3
import toucan_helpers as toucan

try:
    lights = toucan.setup()

    toucan.brightPulse(lights, 0, 0, 100)

    toucan.lightsOut(lights)

except Exception as e:
    print(e)

finally:
    toucan.gpioClean()
