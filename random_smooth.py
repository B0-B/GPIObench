from tools.rgb import RGBLED, randomColor
from time import sleep


'''
RGB led which fades colors like a rainbow.
'''

pins = (2,3,4)
current_color = randomColor()
RGB = RGBLED(*pins)

RGB.on()
RGB.color(*current_color)

while True:
    sampled_color = randomColor()
    RGB.transition(current_color, sampled_color, duration=1)
    print(*sampled_color)
    current_color = sampled_color
    sleep(5)