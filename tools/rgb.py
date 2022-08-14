#!/usr/bin/env python3

from gpiozero import LED, PWMLED
import numpy as np
from time import sleep
from os import path
from random import uniform

def randomColor ():
    return [np.random.choice(255) for i in range(3)]

def stopRequested ():
    '''
    A global function for determining the global operating state to link it to stop.py.
    When stop.py is called in an ext. runtime this function will always return false. 
    '''
    with open(path.dirname(__file__) + '/switch.txt', 'r') as f:
        if f.read() == '1':
            return True
        return False

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
        self.switchPath = path.dirname(__file__) + '/switch.txt'
        self.setSwitch(False)

    def color (self, r, g, b):

        f = 1/255
        c = np.array([r, g, b]) * f
        for i in range(3):
            self.value(c[i], self.colors[i])

    def fade (self, frequencies=None, phase=[0,0,0], colors='rgb', duration=None, loop_frequency=60, strength=[1,1,1]):

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
                
                self.value(strength[i]*state[i], colors[i])

            # update time
            t += T
            
            if duration and t > duration:
                return 

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

    def pulse (self, color=(255,255,255), frequency=1, duration=None):

        self.fade((frequency, frequency, frequency), strength=(color[0]/255, color[1]/255, color[2]/255), duration=duration)

    def setSwitch (self, boolean):

        self.stop = boolean
        with open(self.switchPath, 'w+') as f:
            if boolean:
                f.write('1')
            else:
                f.write('0')

    def stop (self):

        self.stop = True
        with open(self.switchPath, 'w+') as f:
            f.write(0)

    def stopRequested (self):

        with open(self.switchPath, 'r') as f:
            if f.read() == '1':
                return True
            return False

    def test (self):

        self.on()
        coldness = 0
        for i in range(100):
            coldness += 0.01
            self.white(coldness)
            sleep(0.02)

        for i in range(3):
            for col in self.colors:
                self.on(col)
                sleep(.33)
                self.off()
        
        self.fade(frequencies=[1, 1, 1], phase=[0, 0.3, 0.8], duration=3)

    def transition(self, from_color, to_color, duration=1):

        dt = 1/60
        T = int(duration/dt)
        colors = [from_color, to_color]
        for i in range(2):
            if not type(colors[i]) is  np.ndarray:
                colors[i] = np.array(colors[i])

        dc_dt = (colors[1]-colors[0])/T

        for t in range(T):
            c = dc_dt * t + colors[0]
            self.color(*c)
            sleep(dt)

    def value (self, _value, colors='rgb'):

        for col in colors:
            self.LED[col].value = 1 - _value

    def white (self, coldness=0):

        # coldness is a parameter from 0 to 1

        color = [
            255*np.exp(-((coldness-0)/1)**2), 
            200*np.exp(-((coldness-0.5)/1)**2), 
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