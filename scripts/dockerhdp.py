#!/usr/bin/python2
import commands
import dockerimages

print "Content-Type: text/html"
print

print """

<!DOCTYPE html>
<html lang="en">
<head>	

	<meta charset="UTF-8">
	<title>Docker | Hadoop</title>
	<link rel="stylesheet" href="../assets/css/bootstrap.min.css">
	<link rel="stylesheet" href="../assets/css/custom.css">

</head>
<body>
	<div class="container ">
	    <form action="" >

	    <div class="form-group">
		<label for="exampleInputEmail1">Choose your Linux Flavour :</label>

"""


print "<select  id='imagename'>"

#imagelist=commands.getoutput("sudo docker images ").split('\n')

imagelist=dockerimages.imagefind()

print imagelist

z=1

for i in imagelist:
	if z==1:
		pass
	else:
		j=i.split()
		print "<option>" + j[0] + ":" + j[1] + "</option>"
	z+=1

print "</select>"


print """
</div> 

		  <div class="form-group">
			<label for="exampleInputEmail1">Master Nodes :</label>
			<input  type="text" class="form-control" value="1" id="exampleInputEmail1" readonly >
		  </div> 
	  	  <div class="form-group">
		 <label for="exampleInputEmail1">Slave Nodes :</label>
		 <input  type="text" class="form-control" id="slavenumber" placeholder="no  of slave" >
	  	</div> 
	  		<input type="button" class="btn btn-primary" onclick="myfunction()" value="Submit" />
	 
    		</form>
         
	 	<form action="dockerh.py" id="output" >
	
	 
    		</form>

	</div>
	

	<script src="../assets/js/jquery.min.js" > </script>
  	
   	<script src="../assets/js/bootstrap.min.js" > </script>

	<script src="../assets/js/docker.js "></script>
 
</body>
</html>

"""
