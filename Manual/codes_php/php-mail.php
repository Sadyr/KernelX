<?php
$to = "example@examole.com";
$subject = "My subject";
$txt = "Hello world!";
$mail->addAttachment('/var/tmp/file.tar.gz');
$headers = "From: info@erado.kz" . "\r\n" .
"CC: info@erado.kz";

mail($to,$subject,$txt,$headers);
echo "Message send";
?>
