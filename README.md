# toucan8

Files for running a [Little Bird Electronics](https://www.littlebird.com.au/products/little-bird-toucan-8-x-apa102-rgb-led) [Toucan 8 LED HAT for Raspberry Pi](https://www.littlebird.com.au/products/little-bird-toucan-8-x-apa102-rgb-led). 

## Notes on the Toucan

* Data Line is on Pin 16 (GPIO23)
* Clock Line is on Pin 18 (GPIO24)
* SPI must be enabled on your Pi (`sudo raspi-config nonint do_spi 0`)
* Works with a library that drives APA102: 
  * pypi - https://pypi.org/project/apa102/
  * blinkt - https://github.com/pimoroni/blinkt
  * Arduino - https://www.arduinolibraries.info/libraries/apa102
* Little Bird forums - https://discourse.littlebird.com.au/search?q=toucan%208

## Notes on this repository

* Requires Python 3
* Scripts tested on a Raspberry Pi 2 Model B, running Raspbian 10 (Buster) with Python 3.7
* I'm a python noob so be kind ;) There's probably a better way to do everything.

## /apa102

Python files using APA102 - https://pypi.org/project/apa102/

Quick start (on your pi):

```bash
cd ~
git clone git@github.com:cheshrkat/toucan8.git
cd toucan8/apa102
pip3 install -r requirements.txt 
python3 toucan-helloworld.py
```

* `toucan-helloworld.py` flashes a simple rainbow on and off, which is good to confirm things are working.
* To preview all the scripts, run `toucan.py`
* To just switch everything off, run `toucan-off.py`
* Review `toucan_helpers.py` to see the various helper functions. Note you need to pass your `lights` object to most of them.
