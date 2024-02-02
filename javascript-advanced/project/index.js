console.log('Tic Tac Toe');

//use event listener when click on the board.

var ticTac = document.querySelectorAll('td');

for( let tac of ticTac){
    tac.addEventListener('click', function(){
        if(tac.innerText === ''){
            tac.innerText = 'X'
        } else if(tac.innerText === 'X'){
            tac.innerText = 'O'
        }else if(tac.innerText === 'O'){
            tac.innerText = 'X'
        }
    })
}

//handle reset
var buttonId = document.getElementById('btnId');
buttonId.addEventListener('click', function(){
    for(let tac of ticTac){
        tac.innerText = ""
    }
})