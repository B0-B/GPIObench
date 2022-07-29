#!/usr/bin/env python3
from tools import *
from gpiozero import LED

# if use a single led connect it to pins 10, 9, 11 to r, g, b resp.

#       r,g,b  r,g,b
pins = [2,3,4,10,9,11]
leds = [LED(pin) for pin in pins]

#RGBLED(leds[3:], r=0, g=0, b=1)
RGBfade(leds, rgb_frequencies=[.005,.005,.005], led_rgb_phase_shift=[0.6, 0.2, 0.4], frequency=50)