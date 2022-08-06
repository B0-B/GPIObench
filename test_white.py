from tools.rgb import RGBLED
from time import sleep

coldness = 0

pins = (2,3,4)
RGB = RGBLED(*pins)

RGB.on()
RGB.white(coldness)

levels = 20

for i in range(levels):
    
    coldness = i/levels
    RGB.white(coldness)
    sleep(0.5)