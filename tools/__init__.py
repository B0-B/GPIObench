
from time import sleep
from random import gauss, uniform, choice
import math




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

def RGBpulse (rgb_pins, color=[1,1,1], frequency=1, min_value=0.0, max_value=1.0, duration=None):
    
    t, T = 0, 1/240
    # global_intensity = 0
    omega = 2*math.pi*frequency
    # c_cum_inv = 1/sum(color)
    osc = lambda t: 0.5 * (math.sin(omega*t) + 1) * (max_value-min_value) + min_value

    while True:

        

        # t_pulse, t_wait = global_intensity * T, (1-global_intensity) * T

        # t_rgb = [t_pulse*color[0]*c_cum_inv, t_pulse*color[1]*c_cum_inv, t_pulse*color[2]*c_cum_inv]
        
        # for i in range(3):
        #     if rgb_pins[i] != 0:
        #         rgb_pins[i].off()

        # for i in range(3):
        #     sleep(t_rgb[i])
        #     rgb_pins[i].on()
        
        # update the time
        t += T

        if duration and t > duration:
            return 

        sleep(t_wait)

def RGBfade (rgb_pins, rgb_frequencies=[.1,.1,.1], frequency=60, duration=None, led_rgb_phase_shift=[0,0,0]):

    '''
    Varies the r,g and b channels with shift between leds and different frequencies for rgb colors.
    '''

    # create new led objects which have 3 different potentials relative to ground
    led_1 = [rgb_pins[0], rgb_pins[1], rgb_pins[2]]
    led_2 = [rgb_pins[3], rgb_pins[4], rgb_pins[5]]

    # define global frequency and rgb frequencies
    omega_list = [2 * math.pi * f for f in rgb_frequencies]

    # initialize loop parameters
    led_rgb_phase_shift = [led_rgb_phase_shift[i] * 2*math.pi for i in range(3)]
    pulse_width = [0, 0, 0, 0, 0, 0]
    T = 1/frequency # a single loop time (simulate AC)
    t = 0

    while True:

        #print(pulse_width)

        # update pulse width of first LED by base frequency
        # LED 1
        for i in range(3):
            pulse_width[i] = (math.sin(omega_list[i] * t) + 1) * 0.5
        
        # update the second led analogous but with a color-dep. phase shift in the sine
        # LED 2
        for i in range(3):
            pulse_width[3+i] = (math.sin(omega_list[i] * t + led_rgb_phase_shift[i]) + 1) * 0.5


        # determine the current pulse time <= T
        t_r_1 = pulse_width[0] * T
        t_g_1 = pulse_width[1] * T
        t_b_1 = pulse_width[2] * T
        t_r_2 = pulse_width[3] * T
        t_g_2 = pulse_width[4] * T
        t_b_2 = pulse_width[5] * T
        t_longest = max(pulse_width) * T
        
        # switch on both LEDs
        for led in [led_2]:
            for i in range(3):
                led[i].off()
        
        # switch off
        dt = max(t_longest/1000, 0.002)
        timesteps = int(t_longest/dt)
        for i in range(timesteps):
            t_cum = i*dt
            if t_cum > t_r_1:
                led_1[0].on()
            if t_cum > t_g_1:
                led_1[1].on()
            if t_cum > t_b_1:
                led_1[2].on()
            if t_cum > t_r_2:
                led_2[0].on()
            if t_cum > t_g_2:
                led_2[1].on()
            if t_cum > t_b_2:
                led_2[2].on()
            sleep(dt)
        
        
        # update time
        t += T

        # check if duration is exceeded, if set.
        if duration and t > duration:
            return
        
        # sleep the rest of the period
        sleep(T-t_longest)