#!/usr/bin/python2

import commands
def cfind(cName):
	if commands.getstatusoutput("sudo docker inspect {0}".format(cName))[0]  == 0:
		return 1
	else:
		return 0

