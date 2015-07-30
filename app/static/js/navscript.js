$(document).ready(function(){

	var out = true;

	$(window).scroll(function() {
		if( $(this).scrollTop() > 150) {
			if( out ){
				$('.nav').animate({'left':'-100px'}, 150);
				$('#menu').animate({'left':'0'}, 150);
				$('#menu-img').css({'-webkit-transform':'rotate(0deg)'});
				out = false;
			};
		} else {			
			if( !out ) {
				$('.nav').animate({'left':'0'}, 150);
				$('#menu').animate({'left':'-100px'}, 150);
				out = true;
			};
		};
	});

	$('#menu').on('click', function(e){
		e.preventDefault();
		if( !out ){
			$('#menu-img').css({'-webkit-transform':'rotate(180deg)'});
			$('.nav').animate({'left':'0'}, 150);
			out = true;
		} else {
			$('.nav').animate({'left':'-100px'}, 150);
			$('#menu-img').css({'-webkit-transform':'rotate(0deg)'});
			out = false;
		};
	});






})