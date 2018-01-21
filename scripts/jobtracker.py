#!/usr/bin/python2
import commands
import cgi
import thread

print "Content-Type: text/html"
print

def ansible():
	print commands.getstatusoutput("sudo ansible-playbook ../ansible/jobtracker.yml  -i ../hostfile/hadoop")
	remove=commands.getstatusoutput("rm -f ../temp/mapred-site.xml")
	remove1=commands.getstatusoutput("rm -f ../temp/core-site.xml")


IPjob=cgi.FormContent()['job'][0]
IP=cgi.FormContent()['master'][0]

s="\n[jobtracker]\n"
s+=IPjob+" ansible_ssh_user=root ansible_ssh_pass=redhat \n"
f1=open('../hostfile/hadoop','a')
f1.write(s)
f1.close()

print IPjob +" and "+IP

def mapp():
	fh=open("../files/mapredjob-site.xml","r")
	s=fh.read()
	fh.close()
	s=s.replace("IPJOB",IPjob)
	ft=open("../temp/mapred-site.xml",'w')
	ft.write(s)
	ft.close()


def core():
	fc=open("../files/core-site.xml","r")
	c=fc.read()
	fc.close()
	c=c.replace("IP",IP)
	fct=open("../temp/core-site.xml",'w')
	fct.write(c)
	fct.close()

mapp()	

core()

ansible()

print commands.getstatusoutput("sudo ansible jobtracker -m command -a 'hadoop-daemon.sh start jobtracker' -i ../hostfile/hadoop ")
print commands.getstatusoutput("sudo ansible jobtracker -m command -a 'hadoop dfsadmin -safemode leave' -i ../hostfile/hadoop")
