<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://plant-health-app-123.vercel.app');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if($_SERVER['REQUEST_METHOD'] === 'POST'){


$url = $_POST['url1'];
$i = $_POST['val'];


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
?>
