
//~ <?php

//~ session_start();


//~ $dbServername = "localhost";
//~ $dbUsername = "root";
//~ $dbPassword = "root";
//~ $dbname = "dbimy320";

//~ $email = $_POST["email"];	//change back
//~ $pass = $_POST["password"];


//~ //echo "XXXXX  display_schae.php XXXXXX";
//~ $conn = new mysqli($dbServername, $dbUsername, $dbPassword, $dbname);

//~ /*
//~ if($conn->connect_error)
//~ {
	//~ die("Connection failed: " . $conn->connect_error);
//~ }
//~ */

//~ $query = "SELECT * FROM tbusers WHERE email = '".$email."' AND pword = '".$pass."';";

//~ $result = mysqli_query($conn, $query);
//~ $row = mysqli_fetch_assoc($result);
//~ /*if (!mysqli_query($conn, $query)) {
	//~ echo 'ERROR';
//~ }*/

//~ $username = $row["username"];
//~ $name = $row["name"];
//~ $lastname = $row["lastname"];



//~ $_SESSION["username"] = $row["username"];
//~ $_SESSION["name"] = $row["name"];
//~ $_SESSION["lastname"] = $row["lastname"];
//~ $_SESSION["email"] = $email = $_POST["email"];
//~ $_SESSION["pass"] = $_POST["password"];

	

//~ header('Location: ../about.html');


		error_reporting(E_ALL);

		$username = $_POST['uname'];
		$pass = $_POST['pword'];


		$conn = mysqli_connect("localhost", "root", "", "dbimy320");

		$sql = "SELECT * FROM tbusers WHERE username = '$username'";
		$result = $conn->query($sql);


		while ($row = $result->fetch_assoc())
		{
			if($username = $row['username'] && $pass = $row['pword'])
			{
				$fname = $row['name'];
				$lname = $row['lastname'];

			    echo "Welcome, ".$fname;
				
				
			}
			else
			{
			    die("incorrect username/password!");
			}
		}
		header('Location: ../splash.html');
		?>			

