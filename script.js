window.addEventListener("load", link_events, false);

var xhr = false; 

function link_events()
{
	document.getElementById("text_input").onkeydown = charcount;
	document.getElementById("text_input").onclick = charcount;
	document.getElementById("text_submit").onclick = newpost;
	xhr = new XMLHttpRequest();
	if(xhr)
	{
		xhr.open("GET", "postexp.xml", true);
		xhr.send(null);	
	}
}

function charcount()
{
	var str = document.getElementById("text_input").value;
	var location = document.getElementById("counter");
	var len = str.length;
	var newstr = len + "/256";
	location.innerHTML = newstr;
}

function newpost()
{
	var location = document.getElementById("sitedat");
    	var oldxml = xhr.responseText;
	var newxml = old
	
	//var str = document.getElementById("text_input").value;
}