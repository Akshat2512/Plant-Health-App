<?php
if(isset($_POST['url1']))
{
$url = $_POST['url1'];
$i = $_POST['val'];

$img = file_get_contents($url);
$file = fopen("captures/IMG$i.jpg", "w");
fwrite($file, $img);
fclose($file);

$command = `C:/xampp/htdocs/php/Plant_Health_App/my-env/Scripts/activate && python "Python_Backend/plant_disease_detection.py" $i && deactivate`;

$output = escapeshellarg($command);

echo $output;


die;
}
if(isset($_POST['url2']))
{   
    $dlt=$_POST['url2'];
    unlink($dlt);
    die;
}
die;
?>
