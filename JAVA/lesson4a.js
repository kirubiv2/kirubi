//Function Parameters.
//Parameters are additional values that require to be passed as arguments whenever you invoke the function.

function greeting(name){
    console.log("Hello " + name + " How are you?")
}
//call/invoke the function
greeting("Harry")//Harry is an argument
greeting("Reynolds")
greeting("Ruby")

console.log("================================================")

//create a function that outputs "my county is Nairobi, Isiolo, Lamu"
function county(place){
    console.log("My county is " + place)
}
county("Nairobi")
county("Isiolo")
county("Lamu")

console.log("=================================================")
//Below is a function with multiple parameters.
function sum(number1, number2){
    let answer= number1+number2
    console.log(`The sum of the numbers is: ${answer}`)
}
sum(number1=40, number2=50);
sum(80, 20);

console.log("=====================================================")

//create a function that is able to accept parameters to calculate the SI of 2 individuals.si=(p*r*t)/100
function si(p, r, t){
    let result= (p*r*t)/100
    console.log(`The simple interest is: ${result}`)
}
si(p=12000, r=4, t=5);
si(p=45000, r=12, t=8);

console.log("===================================================")

