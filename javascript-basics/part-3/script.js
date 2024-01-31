// Comparison operator

// the three equal is testing if the data type is the same 
console.log(2 === '2')

// the two equal is testing the value compare
console.log(2 == '2')

// same applies for not equal
console.log(5 !== '5')

console.log(5 != '5')


//Control Flow
//if, else-if, while loop, do-while loop
 var isTrue = true;

 if(isTrue){
    console.log('The statement is true')
 } else{
    console.log('The statement was false')
 }

 var numWhile = 1;

//only print number that can be divided by 2
 while (numWhile < 11) {
    if(numWhile%2 === 0){
        console.log(numWhile);
    }
    numWhile+=1
 }

 const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
 for(let i = 0; i < daysOfWeek.length; i++){
    console.log(daysOfWeek[i]);
 }

 //Another way to do a for loop
//  for(let day of daysOfWeek){
//     console.log(day);
//  }