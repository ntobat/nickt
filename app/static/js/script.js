$(document).ready(function(){

	$('.navlink').on('mouseenter', function(){
		$(this).find('.txt').fadeIn(200);
	});
	$('.navlink').on('mouseleave', function(){
		$(this).find('.txt').fadeOut(100);
	});



})