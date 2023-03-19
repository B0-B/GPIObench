from gpiozero import MCP3008, LED
from time import sleep

# analog to digital converter
diode = LED(10)
#diode = MCP3008(channel=0, select_pin=10)

while True:

    print('diode voltage:', diode.value, end='\r')
    sleep(10)