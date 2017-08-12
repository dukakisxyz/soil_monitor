import os
from time import sleep
import RPi.GPIO as GPIO

#--//-- GPIO initialization --//--
pin=18
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.IN)


#--//-- Logic --//--

def callback(pin):  
	if GPIO.input(pin):
		print ("Dry")
	else:
		print ("Moist")

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(18, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(18, callback)

while True:
	# This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
	sleep(2)