<?php
  echo "<html>";
  echo "<head>";
  echo "<title>POST Message Body</title>";
  echo "</head>";
  echo "<body>";

  echo "<h1>POST Message Body</h1>";
  foreach ($_POST as $key => $value) {
        echo "Message [".$key."] Body:".$value;."\n<br/>";
    }

  echo "</body>";
  echo "</html>";
?>
