#!/usr/bin/env python3

from gpiozero import LED
from tools import RGBpulse

pins = [10, 9, 11]
leds = [LED(pins[0]), LED(pins[1]), LED(pins[2])]
rgb = [0, 0, 55]

RGBpulse(leds, rgb, 1)