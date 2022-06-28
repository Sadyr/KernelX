<?php
						$terms = get_terms( 'gazovie_kotel' );

if( $terms && ! is_wp_error($terms) ){
	foreach( $terms as $term ){
		$url = get_term_link( $term );
		echo "<p><a   href='$url' class='list-group-item list-group-item-action text-center' >". $term->name ."</a></p>";
			}
}
?>
