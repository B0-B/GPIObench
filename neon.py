from tools import *
from gpiozero import LED
from tools import fluorescentTube

pin = 17
led = LED(pin)

#blink(led, 1)
fluorescentTube(led, f_min=40, f_max=60, disturb=0.02, duration=None, width=.55, loopPeriod=2, fadeTime=1.1)
