#!/usr/bin/python2
import commands

def imagefind():
	imagelist=commands.getoutput("sudo docker images ").split('\n')
	return imagelist
