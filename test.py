#!/usr/bin/env python3
from tools.rgb import RGBLED

'''
Runs a few programs to check LED functionality.
'''

pins = (10,9,11)
RGB = RGBLED(*pins)
RGB.test()