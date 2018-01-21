#!/usr/bin/python2

import commands
import cgi
import re

print "content-type: text/html"
print


dirName=cgi.FormContent()['dirName'][0]

dirName = dirName.replace(' ','\ ')
removestatus=commands.getstatusoutput("sudo hadoop fs -rmr {}".format(dirName))

if removestatus[0]  == 0:
	if dirName.count('/')==1 :
		print "<script>window.location.href = 'hdfs.py'; </script>"		
	else :	
		dirName = re.search('^[/].*[/]',dirName).group()
		print "<script>window.location.href = 'hdfs.py?dirName={}'; </script>".format(dirName)
else:
	print dirName
	print "not removed"
