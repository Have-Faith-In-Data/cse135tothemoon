<?php
  echo "<html>";
  echo "<head>";
  echo "<title>GET Message Body</title>";
  echo "</head>";
  echo "<body>";
  unset($_COOKIE['username']);
  setcookie('username', null, -1, '/');
  setcookie('username', "");
  // $_COOKIE['username'] = "";
  echo "<h1>Sessions destroyed</h1>";
  echo $_COOKIE['username'];

?>
