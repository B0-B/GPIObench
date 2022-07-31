from tools.rgb import RGBLED
from time import sleep

coldness = 0

pins = (10,9,11)
RGB = RGBLED(*pins)

RGB.on()

for i in range(100):
    coldness += 0.01
    RGB.white(coldness)
    sleep(0.5)