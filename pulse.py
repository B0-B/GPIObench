#!/usr/bin/env python3

from tools.rgb import RGBLED

'''
RGB led pulsating.
'''

pins = (10,9,11)
color = (255, 160, 56)

RGB = RGBLED(*pins)
RGB.pulse(color=color)