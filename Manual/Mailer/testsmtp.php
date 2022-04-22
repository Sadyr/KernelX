<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'testsmtp/PHPMailer-master/src/Exception.php';
require'testsmtp/PHPMailer-master/src/PHPMailer.php';
require 'testsmtp/PHPMailer-master/src/SMTP.php';

// Настройки сервера на примере Яндекс почты
$mail = new PHPMailer;
$mail->isSMTP();                                     
$mail->Host         = 'smtp.gmail.com';
$mail->Port         = 587;
$mail->SMTPAuth     = true;
$mail->Username     = 'sadyr0012@gmail.com'; // Если почта для домена, то логин это полный адрес почты
$mail->Password     = 'uCmLJHB6';
$mail->SMTPSecure   = 'TLS';


// Авторизация
$mail->CharSet = 'UTF-8';
$mail->From = 'test@beltank.kz';
$mail->FromName = 'test@beltank.kz';
$mailadr = $_POST['email'];
$mail->addAddress($mailadr);


// Контент                   
#$mail->isHTML(true);                    
#$mail->Subject = 'Тест отправки через SMTP';
$mail->Body    = $_POST['message'];
#$email = $_POST['email']; // this is the sender's Email address
$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];

// Отправка
if(!$mail->send()) {
    echo 'Сообщение не может быть отправлено.';
    echo 'Ошибка: ' . $mail->ErrorInfo;
    exit;
}
else{
    echo 'Сообщение отправлено по адресу.';
	echo $mailadr;
}
?>
