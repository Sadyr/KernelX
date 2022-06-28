<!--  start footer and bottom navbar -->

    <footer id="footer">
        <div class="container-fluid"></div>
           <div class="navibar d-flex justify-content-center fw-bold ">			   
			    <?php wp_nav_menu(array(
	         'theme_location'=> 'bottom',
	         'container' => null,
	         'menu_class' => '',
	          /* navbar-nav navbar nav-item fw-bold nav-link headerNavMenu */
	       ));?>   
           </div> 
    </footer>

<!--  finish footer and bottom navbar -->

<script src="js/bootstrap.bundle.min.js"></script>

</body>
</html>
