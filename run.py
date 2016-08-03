import subprocess
cmd = ["java", "-jar", "craftbukkit.jar"]
while True:
	print "STARTING THE SERVER --------------------------------------------------------------------------------------------(python)"
	p = subprocess.Popen(cmd)
	#for line in iter(p.stdout.readline, b''): print line,
	p.wait()
	print p.returncode
