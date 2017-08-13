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
	if (GPIO.input(INPUT_PIN) == True):
		print('3.3')
	else:
		print('0')
	sleep(1);

"""
def callback(pin):  
	if GPIO.input(pin):
		print ("State 1")
	else:
		print ("State 2")

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(18, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(18, callback)

while True:
	sleep(2)
"""

