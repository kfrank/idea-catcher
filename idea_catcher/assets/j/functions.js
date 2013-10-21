//$(document).ready(function() {

$(document).ready(function(){
  $('.get-random').click(function(){
    $.ajax({
        type: 'GET',
        url: 'http://ideacatcher.herokuapp.com/random/',
        async: false,
        //processData: false,
        dataType: 'jsonp',
        jsonp: false,
        jsonpCallback: "myJsonMethod",
        success: function(data) { console.log('Success!'); },                                                                                                                                                                                       
        error: function(error,data) { console.log('Uh Oh!', error, data); },
        response: function(error,data) { console.log(error, data); }
    });
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
