#!/usr/bin/python2


import commands

print "content-type: text/html"
print

print """
	<head>
		<meta http-equiv="refresh" content="30">
		<title>Docker Manager</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="../assets/css/bootstrap.min.css">
		<link rel="stylesheet" href="../assets/css/custom.css">
		<script src="../assets/js/jquery.min.js" > </script>
   		<script src="../assets/js/bootstrap.min.js" > </script>

	</head>
"""

print """
<script>
function Check(stat,mycname)
{

	if (stat=="Start")
		document.location='docker_start.py?x=' + mycname;
	else if (stat=="Stop")
		document.location='docker_stop.py?x=' + mycname;
	else if (stat=="Remove")
		document.location='docker_remove.py?x=' + mycname;

}
</script>
"""


print "<table  class='table' style='color:black;'>"
print "<tr class='active'><th>Image Name</th><th>IP Address</th><th>ContainerName</th><th>Status</th><th>Stop</th><th>Start</th><th>Remove</th></tr>"

z=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
	if z == 1:
		z+=1
		pass
	else:
		j=i.split()
		cStatus=commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
		IP=commands.getstatusoutput("sudo docker inspect "+j[-1]+" |  jq '.[].NetworkSettings.Networks.bridge.IPAddress'")[1].strip('"')
		if cStatus=='"exited"' :
			print """

<tr class='danger'>
	<td>""" + j[1] + """</td>
	<td>""" + IP + """</td>
	<td>""" + j[-1] + """</td>
	<td>Exited</td>
	<td><input name='"""+j[-1]+"""' value='Stop' type='button' onclick=Check(this.value,this.name) class='btn btn-warning' disabled/></td>
	<td><input name='"""+j[-1]+"""' value='Start' type='button' onclick=Check(this.value,this.name) class='btn btn-success'/></td>
	<td><input name='"""+j[-1]+"""' value='Remove' type='button' onclick=Check(this.value,this.name) class='btn btn-danger' /></td>
</tr>"""
		else :
			print """
<tr class='success'>
	<td>""" + j[1] + """</td>
	<td>""" + IP + """</td>
	<td>""" + j[-1] + """</td>
	<td>Running</td>
	<td><input name='"""+j[-1]+"""' value='Stop' type='button' onclick=Check(this.value,this.name) class='btn btn-warning'/></td>
	<td><input name='"""+j[-1]+"""' value='Start' type='button' onclick=Check(this.value,this.name) class='btn btn-success' disabled/></td>
	<td><input name='"""+j[-1]+"""' value='Remove' type='button' onclick=Check(this.value,this.name) class='btn btn-danger' /></td>
</tr>"""

print "</table>"
