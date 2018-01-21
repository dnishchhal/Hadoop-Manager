#!/usr/bin/python2
import commands
import cgi
import thread


print "Content-Type: text/html"
print

def ansible():
	ansible=commands.getstatusoutput("sudo ansible-playbook ../ansible/master.yml  -i ../hostfile/hadoop ")
	remove=commands.getstatusoutput("rm -f ../temp/hdfs-site.xml")
	remove1=commands.getstatusoutput("rm -f ../temp/core-site.xml")


folder_name=cgi.FormContent()['folder'][0]
IP=cgi.FormContent()['ip'][0]

f1=open('../hostfile/hadoop','w+')
s="\n[master]\n"
s+=IP+" ansible_ssh_user=root ansible_ssh_pass=redhat"
f1.write(s)
f1.close()

def master():
	fh=open("../files/hdfsname-site.xml","r")
	s=fh.read()
	fh.close()
	s=s.replace("folder_name",folder_name)
	ft=open("../temp/hdfs-site.xml",'w')
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

thread.start_new_thread(master,())

thread.start_new_thread(core,())


ansible()

commands.getstatusoutput("sudo ansible master -m command -a 'hadoop namenode -format' -i ../hostfile/hadoop")
commands.getstatusoutput("sudo ansible master -m command -a 'hadoop-daemon.sh start namenode' -i ../hostfile/hadoop ")
