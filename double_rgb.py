from tools.rgb import RGBLED, thread
from numpy import pi, array
from time import sleep

pin_1 = (2,3,4)
pin_2 = (24,23,18)
f = 0.1
delay = 0.1

colorState_1 = [0, 0.333, 0.666]
colorState_2 = [
    (0+phaseShift)%1, 
    (0.333+phaseShift)%1, 
    (0.666+phaseShift)%1
]

RGB_1 = RGBLED(*pin_1)
RGB_2 = RGBLED(*pin_2)

def t_1 ():
    RGB_1.fade(frequencies=[f, f, f], phase=colorState_1)

def t_2 ():
    RGB_2.fade(frequencies=[f, f, f], phase=colorState_1)

thread(t_1)
sleep(delay % (1/f))
thread(t_2)