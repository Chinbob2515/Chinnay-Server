import os

files = [i for i in os.listdir(".") if not i == "run.py"]

for fileN in files:
	text = ""
	with open(fileN, "r") as file:
		text = file.read()
	text2 = ""
	for line in text.split("\n"):
		if line.startswith("fuelBurnRate"):
			text2 += "\n" + line.split(":")[0] + ": " + str(float(line.split(":")[1])/5)
		else:
			text2 += "\n" + line
	with open(fileN, "w") as file:
		file.write(text2)
