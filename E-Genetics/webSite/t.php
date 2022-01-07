<?php   
// This is the data you want to pass to Python
$result = shell_exec('python3 trial.py not.csv');
$resultData = json_decode($result, true);
echo ($resultData['value']);
?>