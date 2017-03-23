import sys

backuplist = sys.argv[1]
with open(backuplist) as file:    
    for i, line in enumerate(file):
        if line.startswith("rsyncing"):
            print(line.strip())
