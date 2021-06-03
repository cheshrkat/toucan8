from apa102 import APA102
import RPi.GPIO as GPIO
import time
import random

def gpioClean():
    print("Cleaning GPIO")
    GPIO.cleanup()

def randRGB():
    return random.randint(0,255)

def setup():
    lights = APA102(8, 23, 24, brightness=0.1)
    # set to off initially
    lightsOut(lights)
    return lights

def setRandom(lights):
    print("Setting random colours")
    for x in range(0,8):
        lights.set_pixel(x, randRGB(), randRGB(), randRGB())
    lights.show()

def lightsOut(lights):
    print("Switching off")
    for x in range(0,8):
        lights.set_pixel(x, 0, 0, 0)
    lights.show()

def fillUp(lights, r=100, g=100, b=100, delay=0.1):
    for x in range(0,8):
        print("Setting pixel " + str(x))
        lights.set_pixel(x, r, g, b)
        lights.show()
        time.sleep(delay)

def fillDown(lights, r=100, g=100, b=100, delay=0.1):
    for x in range(7,-1,-1):
        print("Setting pixel " + str(x))
        lights.set_pixel(x, r, g, b)
        lights.show()
        time.sleep(delay)

def setAll(lights, r=100, g=100, b=100):
    print("Setting all pixels")
    for x in range(0,8):
        lights.set_pixel(x, r, g, b)
    lights.show()

