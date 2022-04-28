<?php
  echo "<html>";
  echo "<head>";
  echo "<title>GET Message Body</title>";
  echo "</head>";
  echo "<body>";

  echo "<h1>get echo</h1>";
  foreach ($_GET as $key => $value) {
        echo "Message [".$key."] Body:".$value."\n<br/>";
    }
  echo "</body>";
  echo "</html>";
?>
