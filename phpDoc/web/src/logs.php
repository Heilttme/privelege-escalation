<?php
if (isset($_GET['filter'])) {
    $filter = $_GET['filter'];
    $command = "grep '$filter' /var/www/html/logs/auth.log 2>&1";
    $output = shell_exec($command);

    if (!$output) {
        echo "<p>No matching logs found.</p>";
    } else {
        echo "<pre>$output</pre>";  
    }
} else {
    echo "<p>No filter provided.</p>";
}
?>

