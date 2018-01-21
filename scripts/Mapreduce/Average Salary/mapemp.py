#!/usr/bin/python2
import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split('\n')
    for key in keys :
        values = ((key.split('$')[1]).split('.')[0]).split(',')
	value = ""	
	for x in values :
		value = value + x
        print( "%s\t%s" % ('Salary', value) )
