#!/usr/bin/env python3

'''
A script which turns off all pins.
'''

from gpiozero import LED

pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]

for pin in pins:
    try:
        LED(pin).on()
    except:
        pass