#!/usr/bin/env python3

'''
A script which turns off all pins.
'''

import RPi.GPIO as GPIO  
from gpiozero import LED
from os import system

pins = [2,3,4,10,9,11]

for pin in pins:
    try:
        LED(pin).off()
        LED(pin).on()
        GPIO.cleanup(pin) 
    except:
        pass

# lastly cleanup the gpios
#GPIO.cleanup() 

exit()