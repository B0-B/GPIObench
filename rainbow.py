#!/usr/bin/env python3
from tools.rgb import RGBLED
from gpiozero import LED

'''
RGB led which fades colors like a rainbow.
'''

pins = (10,9,11)
RGB = RGBLED(*pins)
RGB.fade(frequencies=[0.01, 0.01, 0.01], phase=[0, 0.3, 0.8])