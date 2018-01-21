#!/usr/bin/python2

import commands
import cgi
import re

print "content-type: text/html"
print

dirName=cgi.FormContent()['dirName'][0]
folderName=cgi.FormContent()['folderName'][0]


dirName = dirName.replace(' ','\ ')
folderName = folderName.replace(' ','\ ')

if dirName.count('/') == 1 :
	makeFolder=commands.getstatusoutput("sudo hadoop fs -mkdir /{}".format(folderName))
else :
	makeFolder=commands.getstatusoutput("sudo hadoop fs -mkdir {}/{}".format(dirName,folderName))	



if makeFolder[0] == 0:
	print "<script>window.location.href = 'hdfs.py?dirName={}'; </script>".format(dirName)
else:
	print makeFolder[1]
	print "not removed"
