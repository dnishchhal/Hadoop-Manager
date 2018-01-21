#!/usr/bin/python2
import commands
import cgi

print "content-type:text/html"
print

ip=cgi.FormContent()['ip'][0]
name=cgi.FormContent()['name'][0]

print ip
print name

s="\n[software]\n"
s+=ip+" ansible_ssh_user=root ansible_ssh_pass=redhat\n"
f=open('../hostfile/software','w+')
f.write(s)
f.close()

f=open('../ansible/software.yml','r')
s=f.read()
s=s.replace('SOFTWARENAME',name)
f=open('../temp/software.yml','w+')
f.write(s)
f.close()

print commands.getstatusoutput("sudo ansible-playbook ../temp/software.yml -i ../hostfile/software")
