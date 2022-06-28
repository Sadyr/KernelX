<!-- start header -->
<!-- finish header -->
<?php
/* 
Template Name: Главная
*/
get_header();
?>
<!-- start top navbar -->
<!-- finish top navbar -->

<!-- start content space -->
    <section class="about ">
        <div class=".container-fluid ">
            <div class="row  p-3 ">
                <div class="col">
                    <h6 class=" p-3 text-center fw-bold">Газовые котлы</h6>
                    <div class=" line"></div>
                    <div class="  mt-n1 list-group">
<?php                        
						$terms = get_terms( 'gazovie_kotel' );

if( $terms && ! is_wp_error($terms) ){
	foreach( $terms as $term ){
		$url = get_term_link( $term );
		echo "<p><a   href='$url' class='list-group-item list-group-item-action text-center' >". $term->name ."</a></p>";
			}
}
?>

				
                          <a href="#" class="list-group-item list-group-item-action text-center">2. third link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center" >3. A fourth link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">4. A second link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">5. third link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center" >6. A fourth link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">7. A second link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">8. third link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center" >9. A fourth link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">10. A second link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">11. third link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center" >12. A fourth link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">13. A second link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">14. third link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center" >15. A fourth link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">16. A second link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center">17. third link item</a>
                          <a href="#" class="list-group-item list-group-item-action text-center" >18. A fourth link item</a>
                      </div>
                </div>
                <div class="col">
                    <h6 class=" p-3 text-center fw-bold">Трубы и фитинги</h6>
                    <div class="line"></div>
                    <div class=" mt-n1 list-group">
                       <?php                        
						$terms = get_terms( 'trubi_i_fitingi' );

if( $terms && ! is_wp_error($terms) ){
	foreach( $terms as $term ){
		$url = get_term_link( $term );
		echo "<p><a   href='$url' class='list-group-item list-group-item-action text-center' >". $term->name ."</a></p>";
			}
}
?>
                        <a href="#" class="list-group-item list-group-item-action text-center">2. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >3. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">4. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">5. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >6. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">7. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">8. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >9. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">10. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">11. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >12. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">13. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">14. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >15. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">16. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">17. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >18. A fourth link item</a>
                      </div>
                </div>
                <div class="col">
                    <h6 class=" p-3 text-center fw-bold">Арматуры</h6>
                    <div class="line"></div>
                    <div class=" mt-n1 list-group">
                        <a href="#" class="list-group-item list-group-item-action text-center">1. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">2. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >3. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">4. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">5. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >6. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">7. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">8. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >9. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">10. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">11. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >12. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">13. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">14. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >15. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">16. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">17. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >18. A fourth link item</a>
                      </div>
                </div>
                <div class="col">
                    <h6 class=" p-3 text-center fw-bold">Противопожарные</h6>
                    <div class="line"></div>
                    <div class=" mt-n1 list-group">
                        <a href="#" class="list-group-item list-group-item-action text-center">1. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">2. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >3. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">4. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">5. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >6. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">7. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">8. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >9. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">10. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">11. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >12. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">13. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">14. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >15. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">16. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">17. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >18. A fourth link item</a>
                      </div>
                </div>
                <div class="col">
                    <h6 class=" p-3 text-center fw-bold">Хомуты | Силиконы |Пены</h6>
                    <div class="line"></div>
                    <div class=" mt-n1 list-group">
                        <a href="#" class="list-group-item list-group-item-action text-center">1. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">2. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >3. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">4. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">5. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >6. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">7. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">8. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >9. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">10. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">11. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >12. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">13. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">14. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >15. A fourth link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">16. A second link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center">17. third link item</a>
                        <a href="#" class="list-group-item list-group-item-action text-center" >18. A fourth link item</a>
                      </div>
                </div>
            </div>
        </div>
		
    </section>



<!-- finish content space -->
<!--  start footer and bottom navbar -->
<!--  finish footer and bottom navbar -->

<?php
get_footer();
?>