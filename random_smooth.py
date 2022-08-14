from tools.rgb import RGBLED, randomColor, stopRequested
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

while not stopRequested():

    # transition to new random color
    sampled_color = randomColor()
    print('new color:', *sampled_color)
    RGB.transition(current_color, sampled_color, duration=transition_duration)
    
    # override current state
    current_color = sampled_color

    # during rest period frequently check for stop requests
    for i in range(rest_duration):
        sleep(1)
        if stopRequested():
            quit() 