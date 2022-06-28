<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon"   href="img/favicon.ico" type="image/x-icon">
    <link rel="stylesheet"  type= "text/css"  href="./assets/css/bootstrap.min.css">
    <link rel="stylesheet" type= "text/css"   href="./style.css">
    <title>
<?php 
if(is_404()) {
echo 'Ошибка 404';
} else {
the_title();
}
?>
	</title>
	<?php
wp_head();
?>
</head>

<!-- start header -->

<body>
    <header>
        <div class="container">
            <div class="row">
                <div class="col-12"> 
                    <h1 class="text-center text-uppercase ">Инжинерная</h1>
                    <h4 class="text-center text-uppercase ">Сантехника</h4>
                </div>
            </div>
        </div>
    </header>


	
 <nav class="navbar sticky-top navbar-expand-lg  ">

        <div class="container-fluid ">
          <a class="navbar-brand fw-bold" href="<?php bloginfo('url');?>"> 
			<?php bloginfo('name');?>
			</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        <div class="collapse navbar-collapse " id="navbarSupportedContent">  
			
         <ul class="navbar-nav  mx-auto ms-auto mb-2 mb-lg-0 ">
          <?php wp_nav_menu(array(
	         'theme_location'=> 'top',
	         'container' => null,
	         'menu_class' => ' navbar-nav navbar nav-item fw-bold nav-link headerNavMenu ',
	          /*navbar-nav navbar nav-item fw-bold nav-link*/
	       ));?>   
         </ul>
			
        </div>        
        </div>       
      </nav>