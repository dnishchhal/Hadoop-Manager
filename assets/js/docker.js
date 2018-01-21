 function myfunction(){
 
	var number = document.getElementById("slavenumber").value
	var image = document.getElementById("imagename").value
	var text='	<div class="form-group"><label for="exampleInputEmail1">Enter the master container name : </label><input  type="text" class="form-control" id="tasknumber" placeholder="Container Name" name="master" ><br><label for="exampleInputEmail1" value="'+number+'">Total slaves '+number+' : </label><input  type="text" class="form-control" name="slave" value="'+number+'" readonly ><br><input  type="text" class="form-control" name="image" value="'+image+'" readonly ><br>'
	
    for (i=0 ; i<parseInt(number) ; i++ ){
	text += '<div class="form-group"><label for="exampleInputEmail1"> Container name of slave'+(i+1)+' :</label><input  type="text" class="form-control" id="exampleInputEmail1" placeholder="container name" name="slavec'+(i+1)+'"></div>'+"<br />"
}

	text+='<input class="btn btn-primary" type="submit" value="SetUp" />'		
	document.getElementById("output").innerHTML = text;

}
