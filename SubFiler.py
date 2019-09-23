print('##########################################################')
print('#                  By Fahd Ab & Hamza Lh                 #')                  
print('#                   @Java-Dreank3rsTeam                  #')
print('##########################################################')
print('-> The in.txt and out.txt fils shoud existe in same path')
print('##########################################################')
import subprocess
import sys

f = open('in.txt').read().split('\n')
m = open("out.txt","w")
for x in f:

	cmd = ['ping', '-c2', '-W 5', x ]
	reached = False
	timeout = 2
	
	while not reached and timeout:
		response = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		stdout, stderr = response.communicate()
		if response.returncode == 0:
			m.write("%s\r\n" % (x))
			reached = True
		else:
			timeout -= 1
	
	
	if not reached:
		print ("\nWait for result...")
m.close()
