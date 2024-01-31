var firstName = prompt("Hello and Welcome. Please enter your firt name:")

var lastName = prompt("Now enter your last name:")

var age = prompt("How old are you?")

var height = prompt("How tall are you in centimeters?")

var petName = prompt("What is your pet name?")



if(firstName[0] === lastName[0] && ( 20 > age < 30) && height >= 170 && petName[petName.length-1] === 'y'){
    console.log("Welcome Comrade! You've passed the Spy test");
} else {
    alert("You can not know my secret")
}