# toucan8

Files for running a [Little Bird Electronics](https://www.littlebird.com.au/products/little-bird-toucan-8-x-apa102-rgb-led) [Toucan 8 LED HAT for Raspberry Pi](https://www.littlebird.com.au/products/little-bird-toucan-8-x-apa102-rgb-led).

## Notes on the Toucan

* Data Line is on Pin 16 (GPIO23)
* Clock Line is on Pin 18 (GPIO24)
* SPI must be enabled on your Pi (`sudo raspi-config nonint do_spi 0`)
* Compatible with Raspberry Pi 3B+, 3, 2, B+, A+, Zero, and Zero W
* Works with a library that drives APA102: 
  * pypi - https://pypi.org/project/apa102/
  * blinkt - https://github.com/pimoroni/blinkt
  * Arduino - https://www.arduinolibraries.info/libraries/apa102
* Little Bird forums - https://discourse.littlebird.com.au/search?q=toucan%208

## /apa102

Python files using APA102 - https://pypi.org/project/apa102/

Quick start:
```bash
pip3 install -r requirements.txt
./toucan.py
```
