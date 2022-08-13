from tools.rgb import RGBLED
from time import sleep

coldness = 0.9

pins = (2,3,4)
RGB = RGBLED(*pins)

RGB.on()
RGB.white(coldness)

while not RGB.stopRequested():
    sleep(1)