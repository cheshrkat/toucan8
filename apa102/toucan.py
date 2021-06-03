#!/usr/bin/env python3
import toucan_helpers as toucan
import time

print("toucan.py")

try:
    lights = toucan.setup()

 #   print("Setting pixels directly")
    # lights.set_pixel(0, 255, 0, 0)  # Pixel 1 to Red
    # lights.set_pixel(1, 0, 255, 0)  # Pixel 2 to Green
    # lights.set_pixel(2, 0, 0, 255)  # Pixel 3 to Blue
    # lights.set_pixel(3, 255, 0, 0)
    # lights.set_pixel(4, 255, 255, 0)
    # lights.set_pixel(5, 255, 0, 255)
    # lights.set_pixel(6, 255, 255, 255)
    # lights.set_pixel(7, 10, 10, 10)
    # lights.show()
    # print("Pausing to admire")
    # time.sleep(1)

    toucan.setRandom(lights)
    time.sleep(0.5)
    toucan.setRandom(lights)
    time.sleep(0.5)
    toucan.setRandom(lights)
    time.sleep(0.5)
    toucan.setRandom(lights)
    time.sleep(0.5)
    toucan.setRandom(lights)
    time.sleep(0.5)
#    toucan.setRandom(lights)
#    time.sleep(0.5)
#    toucan.setRandom(lights)
#    time.sleep(0.5)

#    toucan.fill(lights, 255, 0, 0)
#    time.sleep(1)
    toucan.fillUp(lights, 0, 255, 0)
    toucan.lightsOut(lights)
#    toucan.fillUp(lights, 0, 255, 0, 0.1)
    toucan.lightsOut(lights)
    toucan.fillUp(lights, 255, 0, 0, 0.1)
#    toucan.lightsOut(lights)
    toucan.fillDown(lights, 0, 255, 0, 0.1)

    toucan.lightsOut(lights)
    toucan.fillDown(lights, 255, 255, 0, 0.1)
    toucan.fillUp(lights, 255, 128, 0, 0.1)
    toucan.fillDown(lights, 255, 0, 0, 0.1)

    toucan.setAll(lights, 0, 0, 255)
    time.sleep(1)

except Exception as e: 
    print(e)

finally:
    toucan.lightsOut(lights)
    toucan.gpioClean()
