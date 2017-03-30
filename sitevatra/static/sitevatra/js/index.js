$(document).ready(function(){
  $('.top-menu li').hover(function(){
     $('ul',this).slideDown(200)}, function(){
  $('ul',this).slideUp(200);
  });

});


