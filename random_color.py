#!/usr/bin/env python3
from tools.rgb import RGBLED
from time import sleep
from random import uniform

'''
RGB led which fades colors like a rainbow.
'''

pins = (2,3,4)
RGB = RGBLED(*pins)

RGB.on()

while True:
    color = [uniform(0,1)*255 for i in range(3)]
    RGB.color(*color)
    print(*color)
    sleep(5)