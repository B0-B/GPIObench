from tools.rgb import RGBLED
from time import sleep

coldness = 0.8

pins = (10,9,11)
RGB = RGBLED(*pins)

RGB.on()
RGB.white(coldness)

while True:
    sleep(1)