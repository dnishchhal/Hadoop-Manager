#!/usr/bin/python2
import commands
import cgi
import containername

print "Content-Type: text/html"
print

masterc=cgi.FormContent()['master'][0]
no=cgi.FormContent()['slave'][0]
image=cgi.FormContent()['image'][0]
check=containername.cfind(masterc)
if check==1:
	print "<h1>{} container-name is already exists </h1>".format(masterc)
	exit()
i=1
names=[]
while i<=int(no):
	a=cgi.FormContent()['slavec'+str(i)][0]
	check=containername.cfind(a)
	if check==1:
		print "<h1>{} container-name is already exists </h1>".format(a)
		exit()
	names.append(a)
	i+=1
print masterc
print no
print image
print names

# code for creating the lvm for slave  nodes

def lvcreate(i):
	global names
	lvhost='docker'
	file1=open('../ansible/lvm.yml', 'r')
	filedata = file1.read()
	filedata = filedata.replace('LVHOST',lvhost)
 	filedata = filedata.replace('lvName',names[i])
	filedata = filedata.replace('lvSize','2')
	file2=open('../temp/lvm.yml', 'w')
	file2.write(filedata)
	file2.close()
	print commands.getstatusoutput("sudo ansible-playbook ../temp/lvm.yml -i ../hostfile/dockerhadoop")

i=0
while i<int(no):
	#lvcreate(i)
	i=i+1

# code for launching the docker



def slavenode(a):
	global names
	print commands.getstatusoutput("sudo docker run -dit --name {0} -v /{1}:/data {2}".format(names[a],names[a],image))
	print commands.getstatusoutput("sudo docker exec "+names[a]+" /usr/sbin/sshd")
	print commands.getstatusoutput("sudo docker exec "+names[a]+" /usr/sbin/httpd")


def masternode():
	global masterc
	print commands.getstatusoutput("sudo docker run -dit --name {0} -v /{1}:/data {2}".format(masterc,masterc,image))
	print commands.getstatusoutput("sudo docker exec "+masterc+" /usr/sbin/sshd")
	print commands.getstatusoutput("sudo docker exec "+masterc+" /usr/sbin/httpd")

masternode()

i=0

while i<int(no):
	slavenode(i)
	i+=1


# copying the files in master

def ansible():
	ansible=commands.getstatusoutput("sudo ansible-playbook master/ansible/master.yml -i master/ansible/hosts ")
	print ansible

IP=commands.getstatusoutput("sudo docker inspect "+masterc+" |  jq '.[].NetworkSettings.Networks.bridge.IPAddress'")[1].strip('"')
print IP
i=0
SIP=[]
while i<int(no):
	a=commands.getstatusoutput("sudo docker inspect "+names[i]+" |  jq '.[].NetworkSettings.Networks.bridge.IPAddress'")[1].strip('"')
	SIP.append(a)
	i+=1
print SIP
def core():
	fc=open("master/files/core-site.xml","r")
	c=fc.read()
	fc.close()
	c=c.replace('masterIp',IP)
	fct=open("master/temp/core-site.xml",'w+')
	fct.write(c)
	fct.close()
def maprd():
	fc=open("master/files/mapred-site.xml","r")
	c=fc.read()
	fc.close()
	c=c.replace('masterIp',IP)
	fct=open("master/temp/mapred-site.xml",'w+')
	fct.write(c)
	fct.close()


fct=open("master/ansible/hosts",'w+')
fct.write(IP+"	ansible_ssh_user=root   ansible_ssh_pass=redhat")
fct.close()


core()
maprd()
ansible()

print "Done"


# copying the files in slave nodes
def ansible1():
	ansible=commands.getstatusoutput("sudo ansible-playbook slave/ansible/master.yml -i slave/ansible/hosts ")
	print ansible

def core():
	fc=open("slave/files/core-site.xml","r")
	c=fc.read()
	fc.close()
	c=c.replace('masterIp',IP)
	fct=open("slave/temp/core-site.xml",'w+')
	fct.write(c)
	fct.close()
def maprd():
	fc=open("slave/files/mapred-site.xml","r")
	c=fc.read()
	fc.close()
	c=c.replace('masterIp',IP)
	fct=open("slave/temp/mapred-site.xml",'w+')
	fct.write(c)
	fct.close()


core()
maprd()

i=0
while i<int(no):
	fct=open("slave/ansible/hosts",'w+')
	fct.write(SIP[i]+"	ansible_ssh_user=root   ansible_ssh_pass=redhat")
	fct.close()
	ansible1()
	i+=1
