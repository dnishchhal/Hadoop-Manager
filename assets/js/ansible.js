 function myfunction(){
 	
	var number = document.getElementById("slavenumber").value
	var text='	<div class="form-group"><label for="exampleInputEmail1">Host Name</label><input  type="text" class="form-control" id="tasknumber" placeholder="Host Name" ><br><label for="exampleInputEmail1">Total IP</label><input  type="text" class="form-control" id="IPS" value="'+number+'" readonly ><br></div>'
	
    for (i=0 ; i<parseInt(number) ; i++ ){
	text += '<div class="form-group"><label for="exampleInputEmail1">IP-Address :</label><input required pattern="^([0-9]{1,3}\.){3}[0-9]{1,3}$" type="text" class="form-control" id="exampleInputEmail1" placeholder="xxx.xxx.xxx.xxx"></div>'+"<br />"
}
text+='<input class="btn btn-primary" type="submit" value="SetUp" />'		
document.getElementById("output").innerHTML = text;
}