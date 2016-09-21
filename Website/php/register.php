<?php

session_start();
error_reporting(E_ALL);


$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbname = "dbimy320";


    $mysqli = mysqli_connect("localhost", "root", "", "dbimy320");

    $name = $_POST["fname"];
    $uname = $_POST["uname"];
    $lastname = $_POST["lname"];
    $email = $_POST["email"];
    $pass = $_POST["password"];


    if ($mysqli->connect_error) 
    {
        die("Connection failed: " . $mysqli->connect_error);
    } 

    
$query = "INSERT INTO tbusers(username, name, lastname, email, pword) VALUES ('".$uname."', '".$name."', '".$lastname."', '".$email."',  '".$pass."');";
	

    //$res = $mysqli->query($query);
    if ($mysqli->query($query) === TRUE) 
    {
        echo "<script type = 'text/javascript'> alert('New record created successfully');</script>";
    } 
    else 
    {
         echo "Error: " . $query . "<br>" . $mysqli->error;
    }
    

header('Location: ../splash.html');?>


?>