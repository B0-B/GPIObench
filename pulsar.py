#!/usr/bin/env python3

from gpiozero import LED, PWMLED
from tools import RGBpulse
from time import sleep

pins = [10, 9, 11]
leds = [PWMLED(pins[0]), PWMLED(pins[1]), PWMLED(pins[2])]

for led in leds:
    led.off()

col = leds[0]
col.on()    

col.value = 0.5
sleep(1)
col.value = 0.75
sleep(1)
col.value = 1.0
sleep(1)