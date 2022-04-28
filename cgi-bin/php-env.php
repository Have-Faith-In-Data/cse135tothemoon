<?php

    echo "<html>";
    echo "<head>";
    echo "<title>Environment Variables</title>";
    echo "</head>";
    echo "<body>";

    echo "<h1>Environment Variables</h1>";

    $env_array = getenv();
    foreach ($_SERVER as $key => $value) {
      echo "$key => $value <br />";
  }
    echo "</body>";
    echo "</html>";

?>
