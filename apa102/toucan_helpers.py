from apa102 import APA102
import RPi.GPIO as GPIO
import time
import random

def gpioClean():
    print("Toucan: cleaning GPIO")
    GPIO.cleanup()

def randRGB():
    return random.randint(0,255)

def setup():
    print("Toucan: setting up lights")
    lights = APA102(8, 23, 24, brightness=0.1)
    # set to off initially
    for x in range(0,8):
        lights.set_pixel(x, 0, 0, 0)
    lights.show()
    return lights

def fill(lights, r=100, g=100, b=100):
    print(f"Toucan: filling with {r} {g} {b}")
    for x in range(0,8):
        lights.set_pixel(x, r, g, b)
    lights.show()

def fillRandom(lights):
    print("Toucan: filling with random colours")
    for x in range(0,8):
        lights.set_pixel(x, randRGB(), randRGB(), randRGB())
    lights.show()

def lightsOut(lights):
    print("Toucan: switching off")
    for x in range(0,8):
        lights.set_pixel(x, 0, 0, 0)
    lights.show()

def fillUp(lights, r=100, g=100, b=100, delay=0.1):
    print(f"Toucan: filling up with {r} {g} {b}")
    for x in range(0,8):
        lights.set_pixel(x, r, g, b)
        lights.show()
        time.sleep(delay)

def fillDown(lights, r=100, g=100, b=100, delay=0.1):
    print(f"Toucan: filling down with {r} {g} {b}")
    for x in range(7,-1,-1):
        lights.set_pixel(x, r, g, b)
        lights.show()
        time.sleep(delay)

def fadeUp(lights):
    print("Toucan: fading up")
    for x in range(0,255):
        for y in range(0,8):
            lights.set_pixel(y, x, x, x)
        lights.show() 

def fadeDown(lights):
    print("Toucan: fading down")
    for x in range(255,0,-1):
        for y in range(0,8):
            lights.set_pixel(y, x, x, x)
        lights.show() 


