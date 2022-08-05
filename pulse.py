#!/usr/bin/env python3

from tools.rgb import RGBLED

'''
RGB led pulsating.
'''

pins = (2,3,4)
color = (188, 33, 14)

RGB = RGBLED(*pins)
RGB.pulse(color=color)