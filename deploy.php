<?php

$commands = array(
	'echo $PWD',
    'ssh-keygen -t ed25519 -C "1149066420@qq.com";;;',
	'whoami',
	'git pull',
	'git status',
	'git submodule sync',
	'git submodule update',
	'git submodule status',
    'test -e /usr/share/update-notifier/notify-reboot-required && echo "system restart required"',
);

$output = "\n";

$log = "####### ".date('Y-m-d H:i:s'). " #######\n";
file_put_contents ('deploy-log.txt', $log, FILE_APPEND);

foreach($commands AS $command){
    // Run it
    $tmp = shell_exec("$command 2>&1");
    // Output
    $output .= "<span style=\"color: #6BE234;\">\$</span> <span style=\"color: #729FCF;\">{$command}<br/></span>";
    
    $output .= htmlentities(trim($tmp)) . "<br/>";

    $log  = "\$ $command\n".trim($tmp)."\n";
    file_put_contents ('deploy-log.txt', $log, FILE_APPEND);
}

echo $output; 

?>