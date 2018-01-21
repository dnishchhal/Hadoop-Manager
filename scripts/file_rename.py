#!/usr/bin/python2

import commands
import cgi
import re

print "content-type: text/html"
print


dirName=cgi.FormContent()['dirName'][0]
newName=cgi.FormContent()['newName'][0]

dirName = dirName.replace(' ','\ ')
newName = newName.replace(' ','\ ')

if dirName.count('/')==1 :
	newName1 = '/' + newName
else :
	newName1 = re.search('^[/].*[/]',dirName).group() + newName

renamestatus=commands.getstatusoutput("sudo hadoop fs -mv {} {}".format(dirName,newName1))

if renamestatus[0]  == 0:
	if dirName.count('/')==1 :
		print "<script>window.location.href = 'hdfs.py'; </script>"		
	else :	
		dirName = re.search('^[/].*[/]',dirName).group()
		print "<script>window.location.href = 'hdfs.py?dirName={}'; </script>".format(dirName)
else:
	print renamestatus[1]
	print "Name Already Exist"
