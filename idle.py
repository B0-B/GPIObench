from tools.rgb import RGBLED, randomColor, stopRequested
from time import sleep

pins = (2,3,4)
current_color = randomColor()
RGB = RGBLED(*pins)

RGB.on()
RGB.color(21,48,39)

while not stopRequested():

    sleep(1)