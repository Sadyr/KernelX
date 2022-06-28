<?php
$servername = "srv-pleskdb54.ps.kz:3306";
$database = "mazaltov_kzkz";
$username = "mazaltov_kzkz";
$password = "_Gu3EI53";
// Создаем соединение
$conn = mysqli_connect($servername, $username, $password, $database);
// Проверяем соединение
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($conn);
?>
