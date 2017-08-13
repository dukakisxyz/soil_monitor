import os
from time import sleep
import RPi.GPIO as GPIO

#--//-- GPIO initialization --//--
pin=18
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.IN)

# Start loop
while True: 
	if (GPIO.input(pin) == True):
		print('3.3V – Dry soil')
	else:
		print('0V – Moist soil')
	sleep(10);

