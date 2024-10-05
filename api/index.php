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

$command = `python ../Python_Backend/plant_disease_detection.py $i`;

$output = escapeshellarg($command);
$output = 

echo $output;

}

?>
