python filterlist.py backuplist | tail -n +1 | python linkgen.py > backuplinks.txt

echo "Done! You can find the backup download link in the file 'backuplinks.txt' in the current directory."
