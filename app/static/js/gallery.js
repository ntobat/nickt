$(document).ready(function(){

	$('li').on('click', function(){
		$('html,body').animate({scrollTop: $('.carousel-wrapper').offset().top}, 350);
		$('.main-wrapper').animate({'height':'600px'}, 100);
		$(this).addClass('highlight');
		var img = $(this).find('img');
		var lg = img.data("large");
		$('#main-img').fadeOut(100, function(){
			$(this).attr('src', lg);
			$(this).fadeIn();
		});
	});

	$('.next').on('click', function(){
		var leftPos = $('#decklist').scrollLeft();
		$('#decklist').animate({scrollLeft:leftPos + 280}, 1000);
	});
	$('.prev').on('click', function(){
		var leftPos = $('#decklist').scrollLeft();
		$('#decklist').animate({scrollLeft:leftPos - 280}, 1000);
	});

})