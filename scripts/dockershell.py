#!/usr/bin/python2
import cgi
import commands
import thread

print "Content-Type: text/html"
print

containername=cgi.FormContent()['containername'][0]
ccmd=cgi.FormContent()['code'][0]
ccmd=ccmd.replace('\r\n','\n')
ccmd=ccmd.split("\n")


def run(name,command):
	result=commands.getstatusoutput("sudo docker exec {0} {1}".format(name,command))
	print "<pre>"
	print result[1]
	print "<pre/><br />"


i=0

while i<ccmd.__len__():
	#thread.start_new_thread(run,(containername,ccmd[i]))
	run(containername,ccmd[i])
	i+=1
