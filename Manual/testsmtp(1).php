<?php
// Подкелючения модуля отправки писем
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'testsmtp/PHPMailer-master/src/Exception.php';
require'testsmtp/PHPMailer-master/src/PHPMailer.php';
require 'testsmtp/PHPMailer-master/src/SMTP.php';

// Настройки сервера на примере гугл почты
$mail = new PHPMailer;
$mail->isSMTP();                                     
$mail->Host         = 'srv-plesk33.ps.kz';
$mail->Port         = 25;
$mail->SMTPAuth     = true;
$mail->Username     = 'test@beltank.kz'; 
$mail->Password     = 'tiKw~687';
$mail->SMTPSecure   = false;


// Авторизация
$mail->CharSet = 'UTF-8';
$mail->From = 'test@beltank.kz';
$mail->FromName = 'test@beltank.kz';
$mailadr = $_POST['email'];
$mail->addAddress($mailadr);


// Контент                   
$mail->Body    = $_POST['message'];
$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];

// Отправка
if(!$mail->send()) {
    echo 'Сообщение не может быть отправлено.';
    echo 'Ошибка: ' . $mail->ErrorInfo;
    exit;
}
else{
    echo 'Сообщение отправлено по адресу.  ';
	echo $mailadr;
	echo '   Проверьте почтовый ящик';
}
?>
