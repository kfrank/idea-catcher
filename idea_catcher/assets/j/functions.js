$(document).ready(function() {
  $('.get').click(function(){
    $('body').removeClass('give-active');
    $('body').addClass('get-active');
    $('.give h1').addClass('entypo-right-open-big');
  });
  $('.give').click(function(){
    $('body').removeClass('get-active');
    $('body').addClass('give-active');
    $('.get h1').addClass('entypo-left-open-big');
  });
});