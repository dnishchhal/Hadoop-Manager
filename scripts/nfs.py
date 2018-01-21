#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
print
ip=cgi.FormContent()['ip'][0]

fh = open("/etc/exports","a+")
fh.write("\n/webcontent" +"    \t "+ip)
fh.close()

print commands.getstatusoutput("sudo systemctl restart nfs")


s="\n[mount]\n"
s+=ip+" ansible_ssh_user=root ansible_ssh_pass=redhat"
fh=open('../hostfile/nfs','w+')
fh.read(s)
fh.close()
nfs="""
- name: Mount webserver
  mount:
    src: 192.168.1.35:/webcontent
    dest: 

"""
commmands.getstatusoutput("sudo ansible-playbook nfs")
