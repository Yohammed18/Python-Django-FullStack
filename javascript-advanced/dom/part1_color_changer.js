var header = document.querySelector("h1")

header.style.color = 'red'

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  // 
  function changeHeaderColor(){
    var colorInput = getRandomColor()
    header.style.color = colorInput
  }

  setInterval("changeHeaderColor()", 2000)


  //Event listener
var headone = document.querySelector("#btn");

console.log("Connected")

headone.addEventListener('mouseover', function(){
    headone.textContent = "Mouse over"
    headone.style.color = 'red'
})

headone.addEventListener('mouseout', function(){
    headone.textContent = "This is header"

})

headone.addEventListener('click', function(){
   console.log("YOU CAME OUT!!!")
})