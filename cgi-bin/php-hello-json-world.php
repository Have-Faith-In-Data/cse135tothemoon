<?php
	
	
	$jsonobj = array("time"=>date(DATE_RFC2822), "IP"=>$_SERVER['REMOTE_ADDR'], "heading"=>"Hello, PHP", "title"=>"Hello, PHP!", "message"=>"This page was generated with the PHP programming Lanuage");
	
	echo "Content-type: text/plain\n";
	echo json_encode($jsonobj);

?>
