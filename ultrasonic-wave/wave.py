import RPi.GPIO as gpio
import time
import requests
import os
from dotenv import load_dotenv
import json


config = load_dotenv()
url = os.getenv('URL')

gpio.setmode(gpio.BCM)

trig = 13
echo = 19

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

try:
	count = 0
	while True :
		if count > 5:
			# test 844
			id = 844
			res = requests.get(url+'/trashcan-id/' + str(id))
			if res.status_code == 200 and len(res.text) > 0:
				params = {"trashcanId": id}
				requests.post(url, json=params)

		gpio.output(trig, False)
		time.sleep(2)

		gpio.output(trig, True)
		time.sleep(0.00001)
		gpio.output(trig, False)

		while gpio.input(echo) == 0 :
			pulse_start = time.time()

		while gpio.input(echo) == 1 :
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17000
		distance = round(distance, 2)

		if distance < 5:
			count += 1
		else:
			count = 0

		print("Distance : ", distance, "cm")
except :
	gpio.cleanup()
