#!/usr/bin/python2
import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split('\n')
    for key in keys :
        value = 1
        print( "%s\t%d" % (key.split(',')[4], value) )
