<?php
if(isset($_POST['url1']))
{
$url = $_POST['url1'];
$url_1 =  $_POST['url2'];
$i = $_POST['val'];

$cap_Dir = $url_1;

// if (!is_dir($cap_Dir)) {
//     mkdir('\captures', 0777, true);
// }
echo $_SERVER['DOCUMENT_ROOT'];
$img = file_get_contents($url);
$file = fopen("$cap_Dir/IMG$i.jpg", "w");
fwrite($file, $img);
fclose($file);

$command = `python "Python_Backend/plant_disease_detection.py" $i`;

$output = escapeshellarg($command);

echo $output;

}

?>
