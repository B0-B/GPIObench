#!/usr/bin/env python3

from gpiozero import LED, PWMLED
import numpy as np
from time import sleep
from os import path


class RGBLED:

    '''
    A wrapped class for RGB LEDs.
    '''

    def __init__ (self, pin_red, pin_green, pin_blue) -> None:
        
        # base parameters
        self.clock_rate = 120
        self.colors = ['r', 'g', 'b']

        # build independent pulse-width-modulated LED pins 
        self.LED = {}
        self.pins = {'r': pin_red, 'g': pin_green, 'b': pin_blue}
        for col in self.colors:
            led = PWMLED(self.pins[col])
            led.on()
            self.LED[col] = led

        # interface parameters for on-the-fly changes
        self.frequencies = [.1,.1,.1]
        self.stop = False
        self.setSwitch(False)

    def color (self, r, g, b):

        f = 1/255
        c = 1 - np.array([r, g, b]) * f
        for i in range(3):
            self.value(c[i], self.colors[i])

    def fade (self, frequencies=None, phase=[0,0,0], colors='rgb', loop_frequency=60):

        # override internal color frequencies, if provided
        if frequencies:
            if not (len(frequencies) == 3 and type(phase) is list) :
                raise ValueError('frequencies must be a list with 3 non-negative floats between 0 and 1.')
            self.frequencies = frequencies

        # define time and initialize state
        start = np.array(phase) * 2 * np.pi
        f = np.array(self.frequencies)
        omega = 2 * np.pi * f
        t, T = 0, 1/loop_frequency

        # start loop
        while not self.stopRequested():

            # update numpy state
            state = 0.5*( np.sin(omega * t + start) + 1 )

            # apply strengths by value and current state
            for i in range(len(colors)):
                
                self.value(state[i], colors[i])

            # update time
            t += T
            
            # wait
            sleep(T)

        # set the stop switch to False again
        self.setSwitch(False)

    def off (self, colors='rgb'):
        
        for col in colors:
            self.LED[col].on()

    def on (self, colors='rgb'):
        
        for col in colors:
            self.LED[col].off()

    def setSwitch (self, boolean):

        self.stop = boolean
        with open(path.dirname(__file__) + '/switch.txt', 'w+') as f:
            if boolean:
                f.write('1')
            else:
                f.write('0')

    def stop (self):

        self.stop = True
        with open(path.dirname(__file__) + '/switch.txt', 'w+') as f:
            f.write(0)

    def stopRequested (self):

        with open(path.dirname(__file__) + '/switch.txt', 'r') as f:
            if f.read() == '1':
                return True
            return False

    def value (self, _value, colors='rgb'):

        for col in colors:
            self.LED[col].value = _value

    def white (self, coldness=0):

        # coldness is a parameter from 0 to 1

        color = [
            255*np.exp(-((coldness-0)/1)**2), 
            255*np.exp(-((coldness-0.5)/1)**2), 
            255*np.exp(-((coldness-1)/1)**2)
        ]

        self.color(*color)
    


if __name__ == '__main__':

    pins = (10,9,11)
    RGB = RGBLED(*pins)

    # blink each color test
    #
    # sleep(1)
    # RGB.on('b')
    # sleep(1)
    # RGB.off()
    # RGB.on('r')
    # sleep(1)
    # RGB.off()
    # RGB.on('g')
    # sleep(1)
    # RGB.value(0.5, 'g')
    # sleep(1)
    # RGB.off()
    
    # fade test
    #
    RGB.fade(phase=[0, 0.3, 0.8])

    sleep(3)