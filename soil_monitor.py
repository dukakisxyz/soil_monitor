import os
from time import sleep
import RPi.GPIO as GPIO

#--//-- GPIO initialization --//--
pin=18
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.IN)

def measurement(pin):  
	if (GPIO.input(pin) == True):
		print('3.3V – Dry soil')
	else:
		print('0V – Moist soil')

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(18, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(18, measurement)

while True:
	sleep(2)