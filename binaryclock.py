#!/usr/bin/env python3
#
#	Matthew Page
#	03/14/2026
#
#	binaryclock.py - Working on trying to make
#		a terminal binary clock in Python.
#
################################################

import time
import os
import subprocess


while True:
	#Linux commands do grab each number from date command
	#and also AM/PM status
	cmd1 = "date | cut -d ' ' -f4 | cut -d ':' -f1 "
	cmd2 = "date | cut -d ' ' -f4 | cut -d ':' -f2 "
	cmd3 = "date | cut -d ' ' -f4 | cut -d ':' -f3 "
	cmd4 = "date | cut -d ' ' -f5 "
	cmd5 = "clear"

	subprocess.run(cmd5)

	#Raw hours, minutes, seconds, and AM/PM captured with
	#above commands
	rawhours 	= 	subprocess.check_output(cmd1, shell=True).rstrip()
	rawminutes 	=	subprocess.check_output(cmd2, shell=True).rstrip()
	rawseconds	=	subprocess.check_output(cmd3, shell=True).rstrip()
	rawampm		=	subprocess.check_output(cmd4, shell=True).rstrip()

	#Converting raw hours, minutes, and seconds to integers
	#and AM/PM into a string that is either AM or PM
	hours 	= int(rawhours.decode('utf-8').strip())
	minutes = int(rawminutes.decode('utf-8').strip())
	seconds = int(rawseconds.decode('utf-8').strip())
	ampm 	= rawampm.decode('utf-8').strip()


	#Checking for PM to add 12 hours
	#unless it is 12:xx PM or if it
	#is 24:00 or 12:00 AM to convert
	#to 00:xx
	if ampm == "PM":
		if hours == 12:
			hours = 12
		elif hours == 24:
			hours = 0
		else:
			hours = hours + 12

	#seperating hours, minutes, and
	#seconds by tens and ones place
	#to prepare for each digit being
	#represented by binary bits
	h1, h2 = divmod(hours,10)
	m1, m2 = divmod(minutes,10)
	s1, s2 = divmod(seconds,10)

	#convert each digit into a 4 bit binary string
	h1 = format(h1, '04b')
	h2 = format(h2, '04b')
	m1 = format(m1, '04b')
	m2 = format(m2, '04b')
	s1 = format(s1, '04b')
	s2 = format(s2, '04b')


	#Test prints
	#print(hours,"\n")
	#print(minutes,"\n")
	#print(seconds,"\n")
	#print(ampm,"\n")

	#print(h1,"\n")
	#print(h2,"\n")
	#print(m1,"\n")
	#print(m2,"\n")
	#print(s1,"\n")
	#print(s2,"\n")

	#Display rows, top to bottom: 8, 4, 2, 1
	rows = ["", "", "", ""]
	for i in range(4):
		rows[i] += f"{h1[i]} {h2[i]} : {m1[i]} {m2[i]} : {s1[i]} {s2[i]}"
		# Replace 1's and 0's with other visuals
		rows[i] = rows[i].replace('1', '[O]').replace('0', '[ ]')
	
	# Print the binary clock display         
	print(" H   H     M   M     S   S ")         
	print("---------------------------")         
	for row in rows:
		print(row)

	time.sleep(1)
