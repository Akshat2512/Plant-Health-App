<?php

if(isset($_POST['url1']))
{
$url = $_POST['url1'];
$i = $_POST['val'];

$cap_Dir = '/tmp/captures';

if (!is_dir($cap_Dir)) {
    mkdir($cap_Dir, 0777, true);
}


$img = file_get_contents($url);
$file = fopen("$cap_Dir/IMG$i.jpg", "w");
fwrite($file, $img);
fclose($file);

if (!empty($i)) {
    $command = escapeshellarg("python Python_Backend/plant_disease_detection.py $i");

    // Check if $command is not empty
    if ($i !== '' || $i !== null) {
        $output = shell_exec($command);
        echo $output;
    } else {
        echo "Error: Command is empty.";
    }
} else {
    echo "Error: Value of $i is null or empty.";
}
} else {
echo "Error: Missing required POST parameters.";
}

?>
