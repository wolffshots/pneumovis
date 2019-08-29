const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// setTimeout(function(){
//     $('#message').fadeOut('slow');
// },5000);

$(document).ready(function(){
    $('.tabs').tabs();
});

// shift f5 to clear the cache and make these changes appear in browser