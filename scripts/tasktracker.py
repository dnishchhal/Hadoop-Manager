#!/usr/bin/python2
import commands
import cgi
import thread

print "Content-Type: text/html"
print

def ansible():
	print commands.getstatusoutput("sudo ansible-playbook ../temp/tasktracker.yml -i ../hostfile/hadoop")
	remove=commands.getstatusoutput("rm -f ../temp/mapred-site.xml")
	remove=commands.getstatusoutput("rm -f ../temp/tasktracker.yml")


IPjob=cgi.FormContent()['job'][0]
task=cgi.FormContent()['task'][0]

print task +" and "+IPjob

def mapp(i):
	f1=open('../ansible/tasktracker.yml','r')
	s=f1.read()
	s=s.replace('SLAVE','slave'+str(i))
	f1.close()	
	f2=open('../temp/tasktracker.yml','w')
	f2.write(s)
	f2.close()	
	fh=open("../files/mapredjob-site.xml","r")
	s=fh.read()
	fh.close()
	s=s.replace("IPJOB",IPjob)
	ft=open("../temp/mapred-site.xml",'w')
	ft.write(s)
	ft.close()

i=1
while i<=int(task):
	mapp(i)	
	ansible()
	print commands.getstatusoutput("sudo ansible slave"+str(i)+" -m command -a 'hadoop-daemon.sh start tasktracker' -i ../hostfile/hadoop")
	i+=1

