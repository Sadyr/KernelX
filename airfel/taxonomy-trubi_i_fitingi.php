<!-- start header -->
<!-- finish header -->
<?php
/* 
Template Name: Таксономии-trubi_i_fitingi
*/
get_header();
?>
<div class="col-md-8">
	<?php
		if(have_posts()) {
			while(have_posts()) {
				the_post();
				
			?>

			<div class="card mb-4">
				<div class="card-body">
					<h2 class="card-title"><?php the_title(); ?></h2>
					<p class="card-text"><?php the_field('Power'); ?></p>
				</div> <?php
				$key_name = get_post_custom_values($key = 'Power');
               echo $key_name[0]; ?>
							</div>
			<?php }
		}
	?>
	</div>
