#!/usr/bin/python2


import cgi
import commands

print "content-type:  text/html"
print

fdata=cgi.FormContent()['fname'][0]
print fdata


fh=open('../upload/data.txt' , 'w+')
fh.write(fdata)
fh.close()


cstatus=commands.getstatusoutput("sudo ansible slave1 -m command -a 'hadoop  fs  -put  ../upload/data.txt   /' -i ../hostfile/hadoop ")

print  cstatus
