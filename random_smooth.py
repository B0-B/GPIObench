from tools.rgb import RGBLED, randomColor
from time import sleep


'''
RGB led which fades colors like a rainbow.
'''

pins = (2,3,4)
current_color = randomColor()
RGB = RGBLED(*pins)

transition_duration = 3
rest_duration = 10

RGB.on()
RGB.color(*current_color)

while True:
    sampled_color = randomColor()
    RGB.transition(current_color, sampled_color, duration=transition_duration)
    print(*sampled_color)
    current_color = sampled_color
    sleep(rest_duration)