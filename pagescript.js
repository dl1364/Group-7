window.addEventListener("load", link_events, false);

function link_events()
{
	document.getElementById("text_input").onkeydown = HelloWorld;
	document.getElementById("text_input").onclick = HelloWorld;
}

function HelloWorld()
{
	var str = document.getElementById("text_input").value;
	var location = document.getElementById("counter");
	var len = str.length;
	var newstr = len + "/256";
	location.innerHTML = newstr;
}

function edit_fun(id, method)
{
	if(method === 0)
	{
		var poststr = "post" + id;
		var editstr = "edit" + id;
	}
	else
	{
		var poststr = "postp" + id;
		var editstr = "editp" + id;
	}
	var postloc = document.getElementById(poststr);
	var editloc = document.getElementById(editstr);
	if(postloc.style.display === "none")
	{
		postloc.style.display = "block";
		editloc.style.display = "none";
	}
	else
	{
		postloc.style.display = "none";
		editloc.style.display = "block";
	}
	
}
