<?php
$name = "не определено";
$age = "не определен";
if(isset($_POST["name"])){
  
    $name = $_POST["name"];
}
if(isset($_POST["age"])){
  
    $age = $_POST["age"];
}
echo "POST запрос успешно отправлен на сервер. Данные были записаны в файл user.txt" ;
#$recorddate ="Имя: $name <br> Возраст: $age" 

$fp = fopen('user.txt', 'a');
fwrite($fp,"Имя: $name \n"); 
fwrite($fp,"Возраст: $age");  
fclose($fp);   
?>
