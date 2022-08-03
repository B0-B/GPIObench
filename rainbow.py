#!/usr/bin/env python3

from tools.rgb import RGBLED

'''
RGB led which fades colors like a rainbow.
'''

pins = (10,9,11)
RGB = RGBLED(*pins)
f = 0.05
RGB.fade(frequencies=[f, f, f], phase=[0, 0.4, 0.8])