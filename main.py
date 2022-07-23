from tools import *
from gpiozero import LED
from tools import fluorescentTube

pin = 17
led = LED(pin)


fluorescentTube(led, f_min=45, f_max=60, disturb=0.05, duration=None, width=0.5, loopPeriod=1, fadeTime=1)