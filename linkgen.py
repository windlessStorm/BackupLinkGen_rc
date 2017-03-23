with open("backuplist_filtered") as file:
	for line in file:
		parts = line.split("/")
		for data in parts:
			if data.startswith("backup"):
            			output = "http://downloadbackup.com.bh-edge-1.webhostbox.net/{0}".format(data)
				print output.strip("\n")
