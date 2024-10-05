<?php

if(isset($_POST['url']))
{
$url = $_POST['url'];
$i = $_POST['val'];
$url_1 = $_POST['url1'];
$cap_Dir = '/tmp/captures';

if (!is_dir($cap_Dir)) {
    mkdir($cap_Dir, 0777, true);
}

$img = file_get_contents($url);
$file = fopen("$cap_Dir/IMG$i.jpg", "w");
fwrite($file, $img);
fclose($file);

print_r(scandir($url_1));

$command = `my-env/Scripts/activate && python "plant_disease_detection.py" $i && deactivate`;
echo $command;

}

?>
