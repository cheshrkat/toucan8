#!/usr/bin/env python3
import toucan_helpers as toucan

try:
    lights = toucan.setup()

    toucan.brightFadeUp(lights)
    toucan.brightFadeDown(lights)
    toucan.brightFadeUp(lights, 10,0,0)
    toucan.pause()
    toucan.brightFadeDown(lights, 10,0,0)
    toucan.brightFadeUp(lights, 0,10,0)
    toucan.pause(0.5)
    toucan.brightFadeDown(lights, 0,10,0)
    toucan.brightPulse(lights, 0,0,100)
    toucan.brightPulse(lights, 0,0,100,5)
    toucan.lightsOut(lights)

except Exception as e:
    print(e)

finally:
    toucan.gpioClean()
