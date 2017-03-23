with open("backuplist_filtered") as file:
	for line in file:
		parts = line.split("/")
		for data in parts:
			if data.startswith("backup"):
				print data.strip("\n")
