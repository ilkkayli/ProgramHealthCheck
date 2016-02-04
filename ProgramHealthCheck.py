#!/usr/bin/env python

#Author ilkkayli
#Checks the status of a certain program and starts it if the program is down.
#Takes name of the executable and path as arguments.

import subprocess
import os

def check_program_status(NameOfProgramExecutable, Path):
	
	cmdArg = '"' + "imagename eq " + NameOfProgramExecutable + '"'
	
	try:
		pids = subprocess.check_output("tasklist /fi " + cmdArg) #checks if the process is running
		
		if NameOfProgramExecutable not in pids:
			subprocess.call([Path + NameOfProgramExecutable])
		else:
			print NameOfProgramExecutable + " is alive!"
		
	except OSError as e:
		pass

#There are two options for scheduling the script. Just comment out the one you won't use.

#Option 1: use this in case you like to schedule this script using a scheduler such as Windows Task Scheduler
#Add program name and path as arguments, like: check_program_status("putty.exe", "C:\\Putty\\")
check_program_status("putty.exe", "C:\\Putty\\")

#option 2: scheduling using a while-loop is also an option. 
if __name__ == '__main__':
	while True:
		#add program name and path as arguments, like:
		#check_program_status("putty.exe", "C:\\Putty\\")
		check_program_status("putty.exe", "C:\\Putty\\")
		time.sleep(10)		#loop interval in seconds

