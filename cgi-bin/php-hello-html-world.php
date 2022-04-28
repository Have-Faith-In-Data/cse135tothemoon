<?php
	echo "<html>";
	echo "<head>";
	echo "<title>Hello, Python!</title>";
	echo "</head>";
	echo "<body>";

	echo "<h1>Steve and Jason were here - Hello, Python!</h1>";
	echo "<p>This page was generated with the PHP programming langauge</p>";

	echo "<p>Current Time: ".date(DATE_RFC2822)."</p>";

	# IP Address is an environment variable when using CGI
	echo "<p>Your IP Address: ".$_SERVER['REMOTE_ADDR']."</p>";

	echo "</body>";
	echo "</html>";

?>
