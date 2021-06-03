#!/usr/bin/env python3
import toucan_helpers as toucan

print("Running toucan-green")

try:
    lights = toucan.setup()

    toucan.fillUp(lights, 0, 255, 0)
    toucan.fillUp(lights, 0, 0, 0)
    toucan.fillUp(lights, 0, 255, 0)
    toucan.fillUp(lights, 0, 0, 0)
    toucan.fillUp(lights, 0, 255, 0)

    toucan.lightsOut(lights)

except Exception as e:
    print(e)

finally:
    toucan.gpioClean()

