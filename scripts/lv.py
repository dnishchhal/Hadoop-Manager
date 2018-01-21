#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
print 

print "hi"

lvContent = cgi.FormContent()

lvName = lvContent['lvName'][0]
lvSize = lvContent['lvSize'][0]

print lvName +" and "+lvSize


file1=open('../ansible/lvm.yml', 'r')
filedata = file1.read()
filedata = filedata.replace('lvName',lvName)
filedata = filedata.replace('lvSize',lvSize)
file2=open('../temp/lvm.yml', 'w')
file2.write(filedata)
file2.close();
print commands.getstatusoutput("sudo ansible-playbook ../temp/lvm.yml -i lvhost")
commands.getstatusoutput("rm -f ../temp/lvm.yml")



