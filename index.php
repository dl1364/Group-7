<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="style.css">
		<script src="script.js"></script>
	</head>
	<body>
		<div id="nav" class="row">
			<div id="search" class="col2"><input type="text" placeholder="User Search.." /></div>
			<div id="account" class="col2">
				<div class="dropdown"><button class="dropbtn">Acc img</button>
					<div class="dropdown-content"><a href="#">(signin/out)</a> <a href="#">(acc page)</a> <a href="#">(acc settings)</a></div>
				</div>
			</div>
		</div>
		<div id="content" class="row">
			<div id="stream">
            	<?php
			
                	/*$dbc = new mysqli("localhost", "root", "23pass", "mydb");
                    	$query = "select * from post_exp";
                    	$result = $dbc->query($query);
                     	while($row = $result->fetch_assoc())*///for when i manage to work out an sql server for now an xml server as an example
			$xml=simplexml_load_file("postexp.xml");//in the meantime using an xml will work just changes some syntax
			foreach($xml->post as $posts)
                     	{
                     		print 
                      		"
                          		<div id=\"exppost\">
                              		<div class=\"post_content\">
                      		";
                      		print $posts->content_text;
                      		print
                      		"
                                	</div>
                          		<div class=\"post_action_bar\">
                              		<div class=\"poster_id\">
                      		";
                      		print $posts->username;
                      		print
                      		"
                                </div>
                          	<div class=\"post_like\">likes
                      		";
                      		print $posts->likes;
                      		print
                      		"
                                       	</div>
                          		<div class=\"post_comment\">comments
                      		";
                      		print $posts->comment;
                      		print
                      		"
                                        </div>
                                  	<div class=\"post_share\">share</div>
                                  	<div class=\"post_edit\">edit</div>
                              		</div>
                          		</div>
					<br>
                      		";
                	}
                ?>
				<div id="newpost"><textarea id="text_input" maxlength="256" cols="64" name="text_input" rows="4">Say something interesting</textarea><br><div id="counter">25/256</div><input type="submit" /></div>
			</div>
			<div id="friends">friend links(this gets loaded from a .js)</div>
		</div>
		<div id="sitedat">sitedata(links to read-mes and such)</div>
	</body>
</html>