#!/usr/bin/env python3
from tools.rgb import RGBLED

'''
Runs a few programs to check LED functionality.
'''

pins = (2,3,4)
RGB = RGBLED(*pins)
RGB.test()