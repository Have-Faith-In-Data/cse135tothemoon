<?php
  echo "<html>";
  echo "<head>";
  echo "<title>GET Message Body</title>";
  echo "</head>";
  echo "<body>";

  echo "<h1>Sessions Page 2</h1>";

  if (isset($_COOKIE['username'], "")) {
    echo "<tr><td>Cookie from Cookie:</td><td>".$_COOKIE['username']."</td></tr>\n";
  }else {
    echo "<tr><td>Cookie:</td><td>None</td></tr>\n";
  }

  echo "<br />";
  echo "<a href=\"/cgi-bin/php-sessions-1.php\">Session Page 1</a>";
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
