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

	#Test prints
	#print(hours,"\n")
	#print(minutes,"\n")
	#print(seconds,"\n")
	#print(ampm,"\n")

	print(h1,"\n")
	print(h2,"\n")
	print(m1,"\n")
	print(m2,"\n")
	print(s1,"\n")
	print(s2,"\n")

	#Testing some display setup
	print("                                                                         ")
	print("                                                                         ")
	print("    88888                                                                ")
	print("    8   8                                                                ")
	print("    88888                                                                ")
	print("    8   8                                                                ")
	print("    88888                                                                ")	
	print("                                                                         ")
	print("    4   4                                                                ")
	print("    4   4                                                                ")
	print("    44444                                                                ")
	print("        4                                                                ")
	print("        4                                                                ")
	print("                                                                         ")
	print("    22222                                                                ")
	print("        2                                                                ")
	print("    22222                                                                ")
	print("    2                                                                    ")
	print("    22222                                                                ")
	print("                                                                         ")
	print("     11                                                                  ")
	print("      1                                                                  ")
	print("      1                                                                  ")
	print("      1                                                                  ")
	print("    11111                                                                ")
	print("                                                                         ")
	print("               H   H     H   H     MM   MM    MM   MM     SSSSS     SSSSS")
	print("               H   H     H   H     M M M M    M M M M     S         S    ")
	print("               HHHHH     HHHHH     M  M  M    M  M  M     SSSSS     SSSSS")
	print("               H   H     H   H     M     M    M     M         S         S")
	print("               H   H     H   H     M     M    M     M     SSSSS     SSSSS")


	time.sleep(1)
