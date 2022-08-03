#!/usr/bin/env python3

from tools.rgb import RGBLED

'''
RGB led pulsating.
'''

pins = (10,9,11)
color = (30, 210, 70)

RGB = RGBLED(*pins)
RGB.pulse(color=color)