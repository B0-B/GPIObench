from gpiozero import MCP3008
from time import sleep

# analog to digital converter
diode = MCP3008(channel=0, select_pin=10)

while True:

    print('diode voltage:', diode.value, end='\r')
    sleep(10)