

$(document).ready(function(){

	$('form').submit(function(e){
		var trunkd = $('textarea').val();
		$('.posts').append("<p>"+trunkd+"</p>")
		alert($('.posts').first().val());
		e.preventDefault();
	});


})

//var trunkd = $.trim('textarea').substring(0,200).trim(this) + "...";
	//	$('.posts').append("<p>"+trunkd+"</p>")
		//e.preventDefault();