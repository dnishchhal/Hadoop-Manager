#!/usr/bin/python2
 
import sys

this_key = None 
last_key = None
running_total = 0
count = 0

for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key, value = input_line.split("\t", 1)
   value = int(value)
 
   if last_key == this_key:
       running_total += value
       count+=1
   else:
       if last_key:
           print( "%s\t%d" % (last_key, running_total) )
       running_total = value
       last_key = this_key
 
if last_key == this_key:
   print( "%s\t%s" % (last_key, str(running_total/count)) )
