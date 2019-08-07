const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


setTimeout(function(){
    $('#message').fadeOut('slow');
},2000);

// shift f5 to clear the cache and make these changes appear in browser