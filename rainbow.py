#!/usr/bin/env python3

from tools.rgb import RGBLED
from tools import thread
'''
RGB led which fades colors like a rainbow.
'''

pins = (2,3,4)
RGB = RGBLED(*pins)
f = 0.05
RGB.fade(frequencies=[f, f, f], phase=[0, 0.333, 0.666], colors='rgb')
