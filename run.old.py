from subprocess import call
while 1:
	try:
		call(["java", "-jar", "craftbukkit.jar"])
	except:
		print "oh no, it was killed"
