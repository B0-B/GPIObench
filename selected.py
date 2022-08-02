
from tools.rgb import RGBLED
from random import choice
from time import sleep

'''
RGB led which randomly picks colors from selected panel.
'''

pins = (10,9,11)
RGB = RGBLED(*pins)
period = 10

RGB.on()

colors = [
    [123, 0, 255],
    [126.61138804110568, 245.83010526916755, 93.53413261420276],
    [28.546681476660204, 64.90000818477739, 57.459343536365125],
    [202.72500475561824, 113.50234398467744, 32.083002440325934]
]

while True:
    color = choice(colors)
    RGB.color(*color)
    sleep(period)
