<?php
if(isset($_POST['url1']))
{
$url = $_POST['url1'];
$i = $_POST['val'];

echo "hello";
if (!is_dir('captures')) {
    mkdir('captures', 0777, true)
}

$img = file_get_contents($url);
$file = fopen("captures/IMG$i.jpg", "w");
fwrite($file, $img);
fclose($file);

$command = `python "Python_Backend/plant_disease_detection.py" $i`;

$output = escapeshellarg($command);

echo $output;

die;
}
die;
?>
