<?php
	echo "Cache-Control: no-cache";
	echo "Content-type: text/html\n\n";
	echo "<html>";
	echo "<head>";
	echo "<title>Hello, Python!</title>";
	echo "</head>";
	echo "<body>";

	echo "<h1>Steve and Jason were here - Hello, Python!</h1>";
	echo "<p>This page was generated with the PHP programming langauge</p>";

	date = datetime.now()
	echo "<p>Current Time: ".date(DATE_RFC2822)."</p>";

	# IP Address is an environment variable when using CGI
	address = socket.gethostbyname(socket.gethostname())
	echo "<p>Your IP Address: ".$_SERVER['REMOTE_ADDR']."</p>";

	echo "</body>";
	echo "</html>";

?>
