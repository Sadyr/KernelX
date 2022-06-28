<!-- start header -->
<!-- finish header -->
<?php
/* 
Template Name: Таксономии-Газовый котел
*/
get_header();
?>
<section class="main-content">
	<h2 class="text-center text-uppercase ">
		  <?php 
		  $current_term = single_term_title( "", false );
		  echo $current_term;
		  ?> </h2>
  <div class="container">
    <div class="row">
		<?php
            if(have_posts()) {
              while(have_posts()) {
                the_post();
               ?>
      <div class="col-lg-4 col-sm-6 mb-3" >
        <div class="product-card">
          <div class="product-thumb">
            <a href="#" > <img src="<?php $value = get_field( 'изображение' );
  echo $value;?>" alt=""> </a>
          </div>
          <div class="product-details">
            <h4><a href="<?php $urlpost = get_permalink() ; echo $urlpost  ?>"><?php the_title(); ?></a></h4>
            <p><?php $value = get_field( 'описание_товара' );
  echo $value;?></p>
            <div class="product-bottom-details d-flex justify-content-between">
              <div class="product-price">
                <h5><?php $power = get_field( 'power' );?> 
 <?php foreach ($power as $key => $value) {
  echo ('Мощность'. '<br>');
    echo ($value . '<br>');
}?>  </h5>
              </div>
              <div class="product-links">
                <a href="<?php echo $urlpost?> " class="btn btn-primary">Добавить в корзину</a>           
              </div>

            </div>
          </div>

        </div> 
      </div>

    
 <?php }
            } ?> 
 
  
    </div>
  </div>

</section>