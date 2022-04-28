<?php
  echo "<html>";
  echo "<head>";
  echo "<title>General Request Echo</title>";
  echo "</head>";
  echo "<body>";

  echo "<h1>General echo</h1>";
  echo "<p><b>HTTP Protocol:</b>".$_SERVER['SERVER_PROTOCOL']."</p>";
  echo "<p><b>HTTP Method:</b>".$_SERVER['REQUEST_METHOD']."</p>";
  echo "<p><b>Query String:</b>".$_SERVER['QUERY_STRING']."</p>";
  if (strcmp($_SERVER['REQUEST_METHOD'], "GET") == 0) {
    foreach ($_GET as $key => $value) {
          echo "Message [".$key."] Body:".$value."\n<br/>";
      }
  }
  if (strcmp($_SERVER['REQUEST_METHOD'], "POST") == 0) {
    foreach ($_POST as $key => $value) {
          echo "Message [".$key."] Body:".$value."\n<br/>";
      }
  }
  echo "</body>";
  echo "</html>";
?>
