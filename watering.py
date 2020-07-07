#!/bin/python

############# Script to run the different water pumps one after each other for defined intervalls #############

import RPi.GPIO as GPIO
import time
from datetime import datetime

print('Setmode GPIO')
GPIO.setmode(GPIO.BCM)

###########################################################
# Define parameters
###########################################################

l_Pods = ['Salat'] #, 'Gurke'] #, 'Zucchini', 'Salat', 'Kraeuter', 'Apfel', 'Petersilie', 'Moehren']
l_GPIO = [24] #, 24] #, 23, 24, 25, 12, 16, 20, 21] # select all GPIOs to use
l_watering_duration = [8] #, 8] #, 3, 3, 3, 3, 3, 3, 3]

sleep_time = 1

###########################################################
# Main script
###########################################################

### Log file

file_object = open('water_log.txt', 'a')
file_object.write('\n\n######################### ' + str(datetime.now().date()) + ' #######################################')

### Set up GPIOs

print('GPIO setup')

for i in l_GPIO:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

### Iterate through pods

time.sleep(2)
print('Start watering')

try:
	for pod, gp, duration in zip(l_Pods, l_GPIO, l_watering_duration):
		print("Watering:", pod)
		start_time = datetime.now()
		file_object.write('\n')
		file_object.write('\n' + str(start_time) + ': Watering: '+ str(pod))
		GPIO.output(gp, GPIO.LOW)
		time.sleep(duration)
		GPIO.output(gp, GPIO.HIGH)
		end_time = datetime.now()
		print("Done.")
		file_object.write('\n' + str(end_time) + ': Done (' + str(end_time - start_time) + ').')
		time.sleep(sleep_time)

except:
	print("An error or exception occured")

finally:
	GPIO.cleanup()

file_object.close()
