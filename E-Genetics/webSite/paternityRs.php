<!DOCTYPE html>
<html lang="en">

    <!-- Basic -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">   
   
    <!-- Mobile Metas -->
    <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
 
     <!-- Site Metas -->
    <title>Paternity Test</title>  
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Site Icons -->
    <link rel="shortcut icon" href="images/icon.png" type="image/x-icon" />
    <link rel="apple-touch-icon" href="images/apple-touch-icon.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- Site CSS -->
    <link rel="stylesheet" href="style.css">
    <!-- Colors CSS -->
    <link rel="stylesheet" href="css/colors.css">
    <!-- ALL VERSION CSS -->
    <link rel="stylesheet" href="css/versions.css">
    <!-- Responsive CSS -->
    <link rel="stylesheet" href="css/responsive.css">



</head>
<body class="barber_version">

    <!-- LOADER -->
    <div id="preloader">
        <div class="cube-wrapper">
		  <div class="cube-folding">
			<span class="leaf1"></span>
			<span class="leaf2"></span>
			<span class="leaf3"></span>
			<span class="leaf4"></span>
		  </div>
		  <span class="loading" data-name="Loading">Genetics</span>
		</div>
    </div><!-- end loader -->
    <!-- END LOADER -->
<?php include 'menu.php' ?>
    <!-- End Sidebar-wrapper -->
 <form method='POST' action=''>
        <!-- Page Content -->
        <div id="page-content-wrapper">
            <a href="#menu-toggle" class="menuopener" id="menu-toggle"><i class="fa fa-bars"></i></a>
			
            <div id="home" class="parallax first-section" data-stellar-background-ratio="0.4" style="background-image:url('images/gg.png');">
                <div class="container-fluid">
                    <div class="row">
							<div class="text-center item">
								<div class="col-md-8 col-md-offset-2 col-sm-12">
									<div class="big-tagline text-center">
										<h2><strong>Genteics</strong><br>
										in Egypt</h2>
                                        <p>Upload csv file</p>
										<input type='file' name='data' value='Upload Data' style='margin-left:200px' class="btn btn-light btn-radius btn-brd grd1 effect-1 butn">    
                                        <input type='submit' name='sub' value='Upload Data' style='margin-left:50px; margin-top:50px' class="btn btn-light btn-radius btn-brd grd1 effect-1 butn">    
                                   
                                    </div>
								</div>
						</div><!-- end section -->
    </div><!-- end wrapper -->

   
</form>
    <!-- ALL JS FILES -->
    <script src="js/all.js"></script>
	<script src="js/responsive-tabs.js"></script>
    <!-- ALL PLUGINS -->
    <script src="js/custom.js"></script>


</body>
</html>



<?php 
   if(isset($_POST['sub'])){
// This is the data you want to pass to Python
$data = array($_POST['data'], 'as', 'df', 'gh');
// Execute the python script with the JSON data
$result = shell_exec('python3 paternityTest.py' . escapeshellarg(json_encode($data)));
// Decode the result
$resultData = json_decode($result, true);

// This will contain: array('status' => 'Yes!')

}
    
?>