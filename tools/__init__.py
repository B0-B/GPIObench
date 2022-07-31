#!/usr/bin/env python3
from time import sleep
from random import gauss, uniform, choice
import math

'''
General tools.
'''

def blink (led, frequency, duration=3, width=0.5):

    '''
    Blink base method.
    '''

    T = int(duration*frequency)
    t1 = width/frequency
    t2 = (1-width)/frequency
    
    for t in range(T):
        
        led.on()
        sleep(t1)
        led.off()
        sleep(t2)

def blinkFadeIn (led, f_min, f_max, duration, width = 0.5):


    T = 0

    factor = (f_max - f_min) / duration

    while T < duration:
        
        f = round(T * factor + f_min, 4)
        interval = 1/f
        pulseInterval = width * interval
        offInterval = (1-width) * interval

        led.on()
        sleep(pulseInterval)
        led.off()
        sleep(offInterval)

        T += interval

def blinkFadeOut (led, f_max, f_min, duration, width=0.5):

    T = 0

    factor = (f_max - f_min) / duration

    while T < duration:
        
        f = round( (duration - T) * factor + f_min, 4)
        interval = 1/f
        pulseInterval = width * interval
        offInterval = (1-width) * interval

        led.on()
        sleep(pulseInterval)
        led.off()
        sleep(offInterval)

        T += interval

def fluorescentTube (led, f_min=40, f_max=50, disturb=0.05, duration=None, width=0.5, loopPeriod=1, fadeTime=1):

    # initialize general parameters
    f = f_min
    expectation = f_max - f_min
    volatility = (expectation - f_min)/2 # this is 2sigma i.e. 95% confidence
    disturbation = 0
    

    if duration:
        T = duration
        t = 0

    while True:

        # override frequency on disturbation
        if disturb:

            # very rarely switch off the led
            if uniform(0,1) < disturb:

                led.off()
                sleep(gauss(loopPeriod*(1+disturbation), 0.2*(1+disturbation)))
                blinkFadeIn(led, f_min/4, f_min, uniform(0, 3))
                continue
            

            # sample a disturbance
            disturbation = abs(gauss(disturb, 0.1*disturb))

            # sample a pulse width
            width = uniform(0.5-disturbation, 0.5+disturbation)

            # go into spontaneous flickering mode
            if uniform(0,1) < disturbation:

                f = round( uniform(f/2,f)*(1+disturbation),2)

        else:
        
            width = 0.5
            
        # sample a round duration
        dt = gauss(loopPeriod*(1+disturbation), 0.2*(1+disturbation))

        # run the base blinking
        blink(led, f, width=width, duration=dt)

        # sample a random base frequency
        f_new = uniform(f_min, f_max)

        # smooth transition (happens likely)
        if not uniform(0,1) < disturbation:
            t_trans = uniform(fadeTime, 0.01+disturbation)
            if f_new > f:
                blinkFadeIn(led, f, f_new, t_trans)
            elif f_new < f: 
                blinkFadeOut(led, f, f_new, t_trans)

        # override frequency
        f = f_new
        
        # check if duration was exceeded
        if duration:
            t += dt
            if t > T:
                return