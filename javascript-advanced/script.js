// Functions

//function with no parameter
function sayHello(){
    console.log('Saying Hello World with no paramater');
}

function sayHelloName(name){
    console.log('Hello '+name);
}


sayHello();
sayHelloName("James")

//function with default parameter 
function helloDefault(name='Vanessa'){
    console.log("Hello "+name)
}

helloDefault()
helloDefault('Smith')


//return function
function multiplication(x, y){
    // local scope
    var result = x*y
    return result
}

//global scope
var v = "GLOBAL V"

var roster = [
    "LeBron",
    "Kevin",
    "Stephen",
    "Giannis",
    "Kawhi",
    "Luka",
    "James",
    "Anthony",
    "Joel",
    "Damian"
  ];


for(let player of roster){
    console.log(player);
}

function remove(){
    var name = prompt("What name would you like to remove")
    var index = roster.indexOf(name)
    roster.splice(index, 1);
    return roster;
}

console.log(remove())

