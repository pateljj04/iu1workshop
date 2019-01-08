import csv
from time import time
from time import sleep
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

def read_temp():
	now = time().strftime('%I:%M:%S %p') # 2:05:01 PM
	temp = sensor.get_temperature()
	return [now, temp]
with open('data.csv', 'w') as f:
	writer = csv.writer(f)
	writer.write_row(['Time', 'Temperature'])
	while True:
		writer.write_row(read_temp())
		print('row was written')
		sleep(1)
