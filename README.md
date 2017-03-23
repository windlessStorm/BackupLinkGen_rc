# BackupLinkGen_rc
No more manually creating those 1000 backup links for whole mega Reseller backup.

Tested and developed for Python 2.6.6. so it needs to be installed to use this.

1. Download this whole project folder to your machine(should have python with required version installed).
2. Edit the file backuplist and add all the default unedited output of the backup generator from backup server.
3. Execute the shell script backuplinkgen.sh by running "sh backuplinkgen.sh"
4. The list of backup download url will be generated and saved in file backuplinks.txt in the same directory.



I have provided one sample file backuplink_test containing a sample default unedited output of the backup generator from backup server for test purpose.
Copy the content of this file to backuplist and run shell script to test how it works.
