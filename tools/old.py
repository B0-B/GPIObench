
from gpiozero import LED
from time import sleep
from random import gauss, uniform

led = LED(17)

# step signal generator

def blink(led, frequency, T):
	for i in range(int(frequency*T)):
		led.on()
		sleep(1/(2*frequency))
		led.off()
		sleep(1/(2*frequency))

def blinkCountDown(duration=10, T_min=0.001, T_max=1):
	
	t = 0
	while t < duration:
		interval =  (duration - t) / duration * T_max + T_min
		led.on()
		sleep(interval/2)
		led.off()
		sleep(interval/2)
		t += interval
		
def fluorescentTube(led, frequency=60, disturbance=0.05):
	
	T = round(1/frequency,2)
	t = T/2
	f = frequency	
	while True:
		
		if uniform(0,1) < disturbance or round != 0:
			
			t_inbetween = abs(gauss(0, 10))
			f_inbetween = uniform(f/2,f)
			
			blink(led, f_inbetween, t_inbetween)
				

			countDownTime = abs(gauss(0, 5))
			blinkCountDown(countDownTime, T_min=1/f, T_max=f_inbetween)
		
		
		led.on()
		sleep(t)
		led.off()
		sleep(t)	

def stepSignal(frequency, width, fadeIn=None):
	
	T = round(1/frequency,2)
	t = width * T
	delta = T - t
	
	if fadeIn:
		blinkCountDown(fadeIn, T_max=1/frequency)
	
	while True:
		led.on()
		sleep(t)
		led.off()
		sleep(delta)



#blinkCountDown(3)
fluorescentTube(led)
#stepSignal(30, 0.1, 10)


    pass