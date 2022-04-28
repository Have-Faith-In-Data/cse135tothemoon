<?php
  echo "<html>";
  echo "<head>";
  echo "<title>GET Message Body</title>";
  echo "</head>";
  echo "<body>";

  echo "<h1>Sessions Page 1</h1>";
  $_COOKIE['username'] = $_POST['username'];
  echo "<tr><td>Cookie:</td><td>".$_COOKIE['username']."</td></tr>\n";

  echo "<br />";
  echo "<a href=\"/cgi-bin/php-sessions-2.php\">Session Page 2</a>";
  echo "<br />";
  echo "<a href=\"../hw2/py-cgiform.html\">CGI Form</a>";
  echo "<br /><br />";

  # Destroy Cookie button
  echo "<form action=\"/cgi-bin/php-destroy-session.php\" method=\"get\">";
  echo "<button type=\"submit\">Destroy Session</button>";
  echo "</form>";

echo "</body>";
echo "</html>";
?>
