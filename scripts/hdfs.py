#!/usr/bin/python2
print "content:type text/html"
print

import commands
import cgi

try :
	dirName = cgi.FormContent()['dirName'][0]
except :
	dirName = '/'

try :
	dataType = cgi.FormContent()['dataType'][0]
except :
	dataType = 'Directory'

print """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta http-equiv="refresh" content="30">
	<title>HDFS  {}</title>
	<link rel="stylesheet" href="../assets/css/bootstrap.min.css">
	<link rel="stylesheet" href="../assets/css/custom.css">
</head>
""".format(dirName.replace('//','/'))

print """
<script>
function Check(opCode,dirName)
{
	if (opCode == 'Remove')
	{
		remCheck = confirm("DELETE : " + dirName + " ?");
		if(remCheck == true)
			document.location='file_remove.py?dirName=' + dirName;
	}
	else if (opCode == 'Rename')
	{
		newName=prompt("Enter New Name");
		if (newName==null||newName=="")
			alert('No Changes Occured');
		else
			alert(newName.length);
			//document.location='file_rename.py?dirName='+dirName+'&newName='+newName;
	}
	else if(opCode== 'newFolder')
	{
		folderName = prompt("Enter Folder Name");
		if (folderName==null||folderName=="")
			alert('No Folder Created');
		else
		{

			document.location='file_make.py?dirName='+dirName+'&folderName='+folderName;
		}
	}
	else
	{
		dirName = dirName.replace(/^.*[\\\/]/, '');
		dirName = dirName.replace(' ','\\\ ');
		document.location='file_make.py?dirName='+dirName+'&fileName='+fileName;
	}

}
</script>
"""

def hdfsDisplay(dirName,dataType) :
	dirName = dirName.replace('//','/')
	dirName = dirName.replace(' ','\ ')
	if dataType=='Directory':
		datas = commands.getstatusoutput("sudo hadoop fs -ls {}".format(dirName))[1].split("\n")
		gotoPath = "<form action='/scripts/hdfs.py'>Goto Path : <input placeholder='eg. /' name='dirName'><input type='submit' class='btn btn-primary' value='Go'></form>"
		newFolder = "<input type=button value='New Folder' name='newbutton' onclick=Check('newFolder','{}') class='btn btn-primary '/>".format(dirName)
		uploadFile = "<form enctype='multipart/form-data' action='file.py' method='POST'><input type='file' name='file' onchange='this.form.submit()' /></form>"
		if datas[0]=='' :
			print "<center><h2>0 Items Found</h2></center> {}......{}......{}<hr />".format(gotoPath,newFolder,uploadFile)
			print "<table  class='table' style='color:black;' >"
			print "<tr class='active' ><th >Item</th><th>Type</th><th>Size</th><th>Permission</th><th>Replications</th><th>Modified</th><th>Owner</th><th>Group</th><th colspan=1>Operations</th></tr>"

		else :
			print "<center><h2>{} Items Found</h2></center> {}......{}......{}<hr />".format(datas[0].split()[1],gotoPath,newFolder,uploadFile)

			datas.pop(0)

			print "<table  class='table' style='color:black;'>"
			print "<tr class='active'><th >Item</th><th>Type</th><th>Size</th><th>Permission</th><th>Replications</th><th>Modified</th><th>Owner</th><th>Group</th><th colspan=2><center>Operations</center></th></tr>"



			for data in datas :
				name = data.split('/')[-1]
				data = data.split()
				remAddr = (dirName+"/"+name).replace('//','/')
				remButton = "<input name='{}' value='Remove' type='button' onclick=Check(this.value,this.name) class='btn btn-danger' />".format(remAddr)
				renameButton = "<input name='{}' value='Rename' type='button' onclick=Check(this.value,this.name) class='btn btn-warning' />".format(remAddr)

				if data[4]=='0' and data[1]=='-' :
					dataType = "Directory"
				else :
					dataType = "File"
				print """
			<tr>
				<td><a href="/scripts/hdfs.py?dirName={0}/{1}&dataType={2}">{1}</a></td>
				<td>{2}</td>
				<td>{3}</td>
				<td>{4}</td>
				<td>{5}</td>
				<td>{6} : {7}</td>
				<td>{8}</td>
				<td>{9}</td>
				<td>{10}</td>
				<td>{11}</td>
			</tr>""".format(dirName,name,dataType,data[4],data[0],data[1],data[5],data[6],data[2],data[3],renameButton,remButton)

	elif dataType=='File':
		filedata = commands.getstatusoutput("sudo hadoop fs -cat {}".format(dirName))[1]
		print """<h3>{}</h3><hr/>
<pre>
{}
</pre>
""".format(dirName.split('/')[-1].replace('\ ',' '),filedata)

# Function Calling

hdfsDisplay(dirName,dataType)
print """
<body>
    <script src="../assets/js/jquery.min.js" > </script>
    <script src="../assets/js/bootstrap.min.js" > </script>
</body>

"""
