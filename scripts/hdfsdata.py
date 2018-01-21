#!/usr/bin/python2
import commands
import cgi
import thread

print "Content-Type: text/html"
print

print "hi"

IP=cgi.FormContent()['ip'][0]

slave=cgi.FormContent()['slaves'][0]

folder_name=cgi.FormContent()['folder1'][0]

lvSize=cgi.FormContent()['size'][0]

print slave +" and "+IP +" and "+folder_name

ips=[]
i=1

s="\n"
while i<=int(slave):
	n='slaveip'+str(i)
	a=cgi.FormContent()[n][0]
	s+="\n[slave"+str(i)+"]\n"
	s+=a+" ansible_ssh_user=root ansible_ssh_pass=redhat\n"
	ips.append(a)
	i+=1

f1=open('../hostfile/hadoop','w+')
f1.write(s)
f1.close()

f1=open('../hostfile/lvhost','w+')
f1.write(s)
f1.close()




def ansible():
	print commands.getstatusoutput("sudo ansible-playbook ../temp/slave.yml  -i ../hostfile/hadoop")
	print commands.getstatusoutput("sudo ansible-playbook ../temp/lvm.yml -i ../hostfile/lvhost")
	remove=commands.getstatusoutput("rm -f ../temp/hdfs-site.xml")
	remove1=commands.getstatusoutput("rm -f ../temp/core-site.xml")
	commands.getstatusoutput("rm -f ../temp/lvm.yml")
	commands.getstatusoutput("rm -f ../temp/slave.yml")

def hdfs():
	fh=open("../files/hdfsdata-site.xml","r")
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
def lvcreate(i):
	lvhost='slave'+str(i+1)
	file1=open('../ansible/lvm.yml', 'r')
	filedata = file1.read()
	filedata = filedata.replace('LVHOST',lvhost)
 	filedata = filedata.replace('lvName',folder_name)
	filedata = filedata.replace('lvSize',lvSize)
	file2=open('../temp/lvm.yml', 'w')
	file2.write(filedata)
	file2.close()

def slaveyml(i):
	file1=open('../ansible/slave.yml','r')
	d = file1.read()
	d = d.replace('SLAVE','slave'+str(i+1))
	file1.close()
	file2=open('../temp/slave.yml','w')
	file2.write(d)
	file2.close()

i=0
hdfs()
core()

while i<int(slave):
	lvcreate(i)
	slaveyml(i)
	ansible()
	print commands.getstatusoutput("sudo ansible slave"+str(i+1)+" -m command -a 'hadoop-daemon.sh start datanode' -i ../hostfile/hadoop")
	i+=1
