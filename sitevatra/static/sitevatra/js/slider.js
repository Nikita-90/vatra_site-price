function theRotator() {
    $('div.slider img').css({opacity: 0.0});
    $('div.slider img:first').css({opacity: 1.0});
    setInterval('rotate()',3000);
};


function rotate() {
    var current = ($('div.slider img.show')?  $('div.slider img.show') : $('div.slider img:first'));
	var next = ((current.next().length) ? ((current.next().hasClass('show')) ? $('div.slider img:first') :current.next()) : $('div img:first'));
	next.css({opacity: 0.7})
	.addClass('show')
	.animate({opacity: 1.0}, 500);

	current.animate({opacity: 0.0}, 500)
	.removeClass('show');
};


$(document).ready(function() {
	theRotator();
});