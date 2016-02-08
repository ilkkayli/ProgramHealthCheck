#!/usr/bin/env python

#!/usr/bin/env python

#Author: ilkkayli
#Monitors the status of a certain program.

import subprocess
import os
import time
from threading import Thread

rawSrc="log.txt" # a log file 

def check_program_status(NameOfProgramExecutable, Path):
	
	cmdArg = '"' + "imagename eq " + NameOfProgramExecutable + '"'
	
	try:
		pids = subprocess.check_output("tasklist /fi " + cmdArg) #checks if the process is running

		if NameOfProgramExecutable not in pids:
			return 1 #returns False if program is not running.
		else:
			return 0 #True if program is running.
		
	except OSError as e:
		pass
	
def init_program(NameOfProgramExecutable, Path):
	#function writes a line with a timestamp whenever program is restarted
	
	#logging
	timestamp = get_time()
	logLine =  "Program has been restarted at : " + timestamp	+ "\n"
	wRawSrc=open(rawSrc,"a")
	wRawSrc.write(logLine)
	wRawSrc.close()
	
	#start the program	
	subprocess.call([Path + NameOfProgramExecutable])
	
	return	

def get_time():
	#function generates a timestamp for logging
	localtime = time.asctime( time.localtime(time.time()) )
	return str(localtime)

'''----------------------------------------Scheduling Options-------------------------------------------------------'''

#There are two options for scheduling the script. Just comment out the one you won't use. I'd prefer the first one,
#but obviously Windows Task Scheduler is a bit tricky to configure sometimes. That's why there is also option 2.

#Option 1: use this in case you like to schedule this script using a scheduler such as Windows Task Scheduler

#Add program name and path as arguments, like:
#status = check_program_status("putty.exe", "C:\\Putty\\")
status = check_program_status("<program_name>", "<program_path>")
if status == 1:
	print "Initializing program..."
	#change arguments below too. Like: init_program("putty.exe", "C:\\Putty\\")
	init_program("<program_name>", "<program_path>")
else:
	print "Program is alive! " 

#Option 2: scheduling using a while-loop is also an option. Uses threading for running subprocess.call method 
'''if __name__ == '__main__':

	while True:
		time.sleep(3)	#loop interval in seconds
		#add program name and path as arguments, like:
		#status = check_program_status("putty.exe", "C:\\Putty\\")
		status = check_program_status("<program_name>", "<program_path>")
		if status == 1:
			print "Initializing program..."
			#set up thread, like: t = Thread(target=init_program, args=(["putty.exe", "C:\\Putty\\"]))
			t = Thread(target=init_program, args=(["<program_name>", "program_path"])) 
			t.start()

		print "Program is alive! " '''