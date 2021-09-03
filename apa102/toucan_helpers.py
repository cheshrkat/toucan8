from apa102 import APA102
import RPi.GPIO as GPIO
import time
import random

def gpioClean():
    print("Toucan: cleaning GPIO")
    GPIO.cleanup()

def pause(delay=1):
    time.sleep(delay)

def randRGB():
    """Returns random RGB value"""
    return random.randint(0,255)

def setup():
    """Initialise the Toucan8 ready for use. Returns APA102 object as 'lights'"""
    print("Toucan: setting up lights")
    lights = APA102(8, 23, 24, brightness=0.1)
    # set to off initially
    for x in range(0,8):
        lights.set_pixel(x, 0, 0, 0)
    lights.show()
    return lights

def setBrightness(lights, brightness=0.1):
    """Set the brightness of all 8 pixels"""
    for x in range(0,8):
      lights.set_brightness(x, brightness)

def fill(lights, r=100, g=100, b=100):
    """Set all 8 pixels to the supplied RGB value"""
    print(f"Toucan: filling with {r} {g} {b}")
    for x in range(0,8):
        lights.set_pixel(x, r, g, b)
    lights.show()

def fillRandom(lights):
    """Set all 8 pixels to random colours"""
    print("Toucan: filling with random colours")
    for x in range(0,8):
        lights.set_pixel(x, randRGB(), randRGB(), randRGB())
    lights.show()

def lightsOut(lights):
    """Set all 8 pixels to RGB 0,0,0/off"""
    print("Toucan: switching off")
    for x in range(0,8):
        lights.set_pixel(x, 0, 0, 0)
    lights.show()

def fillUp(lights, r=100, g=100, b=100, delay=0.1):
    """Sequence that 'fills up' one pixel at a time with the supplied RGB"""
    print(f"Toucan: filling up with {r} {g} {b}")
    for x in range(0,8):
        lights.set_pixel(x, r, g, b)
        lights.show()
        time.sleep(delay)

def fillDown(lights, r=100, g=100, b=100, delay=0.1):
    """Sequence that 'fills down' one pixel at a time with the supplied RGB"""
    print(f"Toucan: filling down with {r} {g} {b}")
    for x in range(7,-1,-1):
        lights.set_pixel(x, r, g, b)
        lights.show()
        time.sleep(delay)

def fadeUp(lights):
    """Fade all 8 pixels from 0 (off) to 255 (white)"""
    print("Toucan: fading up")
    for x in range(0,255):
        for y in range(0,8):
            lights.set_pixel(y, x, x, x)
        lights.show() 

def fadeDown(lights):
    """Fade all 8 pixels from 255 (white) to 0 (off)"""
    print("Toucan: fading down")
    for x in range(255,0,-1):
        for y in range(0,8):
            lights.set_pixel(y, x, x, x)
        lights.show() 

def brightFadeUp(lights, r=1, g=1, b=1):
    """Step up from 0 to 1.0 brightness in 100 steps"""
    print("Toucan: fading up using brightness")
    setBrightness(lights, 0)
    fill(lights, r, g, b)
    for y in range(0,101,1):
      current_step = float(y/100)
      for x in range(0,8):
        lights.set_brightness(x, current_step)
      lights.show() 

def brightFadeDown(lights, r=1, g=1, b=1):
    """Step from 1.0 to 0 brightness in 100 steps"""
    print("Toucan: fading down using brightness")
    setBrightness(lights, 1)
    fill(lights, r, g, b)
    for y in range(101,0,-1):
      current_step = float(y/100)
      for x in range(0,8):
        lights.set_brightness(x, current_step)
      lights.show() 

def brightPulse(lights, r=1, g=1, b=1, hold=0):
    """Does a bright fade up, optionally pauses at the brightest point, then fades down"""
    print(f"Toucan: starting brightPulse with {r},{g},{b}")
    brightFadeUp(lights, r, g, b)
    if (hold > 0):
        print(f"Toucan: holding brightPulse at peak for {hold}")
        pause(hold)
    brightFadeDown(lights, r, g, b)
    print(f"Toucan: end of brightPulse with {r},{g},{b}")

