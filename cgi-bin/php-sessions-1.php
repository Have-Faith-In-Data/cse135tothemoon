<?php
  echo "<html>";
  echo "<head>";
  echo "<title>GET Message Body</title>";
  echo "</head>";
  echo "<body>";

  echo "<h1>Sessions Page 1</h1>";

  if (strcmp($_POST['username'], "") != 0) {
    echo "<tr><td>Cookie:</td><td>".$_POST['username']."</td></tr>\n";
  } elseif (strcmp($_SERVER['HTTP_COOKIE'],"destoryed") != 0) {
    echo "<tr><td>Cookie from Cookie:</td><td>".$_SERVER['HTTP_COOKIE']."</td></tr>\n";;
  }else {
    echo "<tr><td>Cookie:</td><td>None</td></tr>\n"
  }


echo "</body>";
echo "</html>";
?>
