#!/usr/bin/python2
import commands
import re
import cgi, os

print "content-type: text/html"
print

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()


# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('Files/'+fn, 'w+').write(fileitem.file.read())



uploadstatus=commands.getstatusoutput("sudo hadoop fs -put Files/{0} /{0}".format(fn.replace(' ','\ ')))

if uploadstatus[0] == 0:
	#if dirName.count('/')==1 :
		#print "<script>window.location.href = 'hdfs.py'; </script>"		
	#else :	
		#dirName = re.search('^[/].*[/]',dirName).group()
	print "<script>window.location.href = 'hdfs.py'; </script>"
else:
	print uploadstatus
	print "not removed"
