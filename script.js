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