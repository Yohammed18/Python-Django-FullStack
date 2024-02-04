$('h1').toggleClass('turnBlue')
$('input').eq(1).attr('type', 'checkbox')
var title = $('button').text()

console.log(title);

$('li').css('color', 'purple')
$('li').css('font-size', '20px')

var newCss = {
    'color' : 'white',
    'background' : 'blue',
    'border' : '20px solid red'
}

var x = $('h1')


// x.css('color', 'red')

// Event methods - src https://api.jquery.com/category/events/

$('h1').click(function(){
    //prints out Hello world in the console. 
    console.log("Hello World");
    $(this).toggleClass('turnRed')
})


$('li').on('dblclick', function(){
    //Changes the text for all li tag
    $(this).text("I was changed")
})

//interacting with the key board
$('input').eq(0).on('keypress',function(event){
    
    if( event.which === 13){
        $('h3').toggleClass('turnBlue')
    }
})

$('p').on('mouseenter', function(){
    $(this).text("lorem")
})

//animation
$('button').on('click', function(){
   
    $('.container').slideUp(3000)
    
})