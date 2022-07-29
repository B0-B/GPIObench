#!/usr/bin/env python3

'''
A script which turns off all pins.
'''

from gpiozero import LED

pins = [2,3,4,10,9,11]

for pin in pins:
    try:
        LED(pin).off()
        LED(pin).on()
    except:
        pass
exit()