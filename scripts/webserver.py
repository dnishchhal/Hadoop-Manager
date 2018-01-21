#!/usr/bin/python2
import commands
import cgi

print "Content-Type : text/html"
print

ip=cgi.FormContent()['ip'][0]
port=cgi.FormContent()['port'][0]

conf="""

scriptalias /scripts/ "/webcontent/scripts/"
documentroot /webcontent

Listen {}

<Directory /webcontent>
require all granted
</Directory>

""".format(port)


s="\n[webserver]\n"
s+=ip+" ansible_ssh_user=root ansible_ssh_pass=redhat"

f1=open('../hostfile/webserver','w+')
f1.write(s)
f1.close()


f=open('../files/cgi.conf','w+')
f.write(conf)
f.close()

print commands.getstatusoutput("sudo ansible-playbook ../ansible/webserver.yml  -i ../ansible/webserver)

"""
# function for conf file of apache web server
def serverconf():
	ip_add = raw_input("enter your ip to deploy : ")

	password = getpass.getpass("Enter the password of "+ip_add+" : ")

	checksoftware.installSoftware("httpd",ip_add,password)

	WebPort = raw_input("Enter port number : ")

	WebDir = raw_input("enter deployment dir : ")

	folderstatus=commands.getstatusoutput("sshpass -p "+password+" ssh "+ip_add+" mkdir {}".format(WebDir))

	if folderstatus[0]==0:
		pass
	else:
		print "deployment directory can not be created"

	WebConfigure = commands.getstatusoutput("sshpass -p "+ password +" ssh "+ip_add+" 'echo -e \"Listen {0}\nDocumentRoot {1}\n<Directory {1}>\nRequire all granted\n</Directory>\" > /etc/httpd/conf.d/myweb.conf' ".format(WebPort,WebDir))

	if WebConfigure[0]== 0:
		print "web service configured"
	else:
		print "not configured..."
	# sending index.html file in deployment directory
	send=commands.getstatusoutput("sshpass -p "+ password +" scp /website/index.html root@{0}:{1}".format(ip_add,WebDir))
	if send[0]== 0:
		print "website deployed sucessfully "
	else:
		print "not configured..."

	# restarting httpd services
	restart=commands.getstatusoutput("sshpass -p " + password + " ssh -o stricthostkeychecking=no -l root " + ip_add +" systemctl restart httpd")
	if restart[0]==0:
		print "httpd restarted.."
	else:
		print "httpd is not restarted ..."
"""
