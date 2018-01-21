 function myfunction(){
 	
	var number = document.getElementById("slavenumber").value
	var text='<div class="form-group"><label for="exampleInputEmail1">Master IP-Address :</label><input required pattern="^([0-9]{1,3}\.){3}[0-9]{1,3}$" type="text" class="form-control" id="exampleInputEmail1" placeholder="xxx.xxx.xxx.xxx" name="ip"><br><label>Total slaves :</label><input type="text" class="form-control" id="exampleInputEmail1" value="'+number+'" name="slaves" readonly ><br> </div>'
	
   for (i=0 ; i<parseInt(number) ; i++ ){
	text += '<div class="form-group"><label for="exampleInputEmail1">Enter the slave'+(i+1)+' IP address :</label><input  type="text" class="form-control" id="exampleInputEmail1" required pattern="^([0-9]{1,3}\.){3}[0-9]{1,3}$" placeholder="xxx.xxx.xxx.xxx" name="slaveip'+(i+1)+'"></div>' + "<br />"
	}
	
	text += '<div class="form-group"><label>Slave </label><br><label for="exampleInputEmail1">Enter the folder name :</label><input  type="text" class="form-control" id="exampleInputEmail1" placeholder="folder-name" name="folder1"></div>' + "<br />"
	
text += '<div class="form-group"><br><label for="exampleInputEmail1">Enter the Volume Size :</label><input  type="text" class="form-control" id="exampleInputEmail1" placeholder="Size" name="size"></div>' + "<br />"

text+='<input class="btn btn-primary" type="submit" value="SetUp" />'		
document.getElementById("output").innerHTML = text;
}

