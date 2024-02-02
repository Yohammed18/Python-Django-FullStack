console.log('Tic Tac Toe');

//use event listener when click on the board.

var ticTac = document.querySelectorAll('td');
var buttonId = document.getElementById('btnId');

// create functions to clear board and add Xs & Os
function clearBoard(){
    for(let tac of ticTac){
        tac.textContent = ""
    }
}

function changeMarker(){
        if(this.innerText === ''){
            this.innerText = 'X'
        } else if(this.innerText === 'X'){
            this.innerText = 'O'
        }else if(this.innerText === 'O'){
            this.innerText = 'X'
        }

}


buttonId.addEventListener('click', clearBoard)

for( let tac of ticTac){
    tac.addEventListener('click', changeMarker)
}