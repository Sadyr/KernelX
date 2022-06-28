<?php
add_action('wp_enqueue_scripts','add_styles');
add_action('wp_footer','add_scripts');
add_action('after_setup_theme','my_menu');



function add_styles() {
	wp_enqueue_style('style',get_stylesheet_uri());
	wp_enqueue_style('style_bootstrap',get_template_directory_uri() . '/assets/css/bootstrap.min.css');
	wp_enqueue_style('style_carts',get_template_directory_uri() . '/assets/css/carts.css');
}
	

function add_scripts() {
	wp_enqueue_script('script',get_template_directory_uri() . '/assets/js/bootstrap.bundle.min.js');
}

function my_menu() {
	register_nav_menu( 'top', 'Меню в шапке' );
	register_nav_menu( 'bottom', 'Меню в подвале' );
}




function get_all_meta($type){
              global $wpdb;
              $result = $wpdb->get_results($wpdb->prepare(
                  "SELECT post_id,meta_key,meta_value FROM wp_posts,wp_postmeta WHERE post_type = %s
                    AND wp_posts.ID = wp_postmeta.post_id", $type
              ), ARRAY_A);
               return $result;
          }




?>
