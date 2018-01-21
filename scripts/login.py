#!/usr/bin/python2
import cgi

print "content-type:text/html"

user="admin"
passwd="admin"
username=cgi.FormContent()['user'][0]
password=cgi.FormContent()['pass'][0]

#print username +" and  "+password
if username==user and password==passwd:
	#print "user login sucess"
	print "location: ../home.html"
	print
else:
	print "location: ../index.html"
	print
