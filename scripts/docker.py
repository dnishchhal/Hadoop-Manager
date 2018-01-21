#!/usr/bin/python2

import commands
import cgi

print "Content-Type:text/html"
print

slave=cgi.FormContent()['slave'][0]
master=cgi.FormContent()['master'][0]
port=cgi.FormContent()['port'][0]
#slave=int(raw_input("Enter the  number of slaves  :  "))
#master=int(raw_input("Enter the  number of master  :  "))
#port=raw_input("Enter the port number :")

i=1
while i<=int(slave):
	status=commands.getstatusoutput("sudo docker run -dit -p "+port+":22 --name slave"+str(i)+" hadoopcentos:d2 ")
	if status[0]==0:
		print "sucessfull!! slave"+str(i)
	else:
		print "error"+str(i)
	i=i+1
		
j=1
while j<=int(master):
	status=commands.getstatusoutput("sudo docker run -dit -p "+port+":22 --name master"+str(j)+" hadoopcentos:d2 ")
	if status[0]==0:
		print "sucessfull!! master"+str(j)
	else:
		print "error"+str(j)
	j=j+1 

