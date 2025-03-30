//Research on functions with parameters.Have two examples.
//Research on arrow functions.



// Task: Write a for loop to print all odd numbers from 1 to 19.
for (let i = 1; i <= 19; i += 2) {
    console.log(i);
}
console.log("======================================================")
// Task: Write a for loop to count down from 10 to 1 and print the numbers in the console.
for (let i = 10; i >= 1; i--) {
    console.log(i);
}
console.log("======================================================")
// Task: Write a for loop to find the largest number in the array: [10, 20, 4, 45, 99, 1].
let numbers = [10, 20, 4, 45, 99, 1];
let largest = numbers[0]; // Start with the first element

for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > largest) {
        largest = numbers[i]; // Update largest if a bigger number is found
    }
}

console.log("The largest number is:", largest);
console.log("======================================================")
// Task: Write a for loop to print the multiplication table of 5 from 5 x 1 to 5 x 10.
for (let i = 1; i <= 10; i++) {
    console.log(`5 x ${i} = ${5 * i}`);
}
console.log("======================================================")


// 1. Students to create a function named sayGoodmorning(), 
//    the function to print/log a message “Goodmorning Dear!”. 
//    Call this function.
function sayGoodmorning() {
    console.log("Goodmorning Dear!");
}

// Calling the function
sayGoodmorning();

console.log("======================================================")
// 2. Students to create a function named myCountry(),  
//    the function to print/log 5 messages explaining about myCountry.  
//    Call this function.
function myCountry() {
    console.log("1. My country is rich in culture and history.");
    console.log("2. It has diverse landscapes, from mountains to beaches.");
    console.log("3. The people are known for their hospitality and kindness.");
    console.log("4. My country has a unique and delicious cuisine.");
    console.log("5. We celebrate many festivals with joy and enthusiasm.");
}

// Calling the function
myCountry();



//A function with parameters allows us to pass values (arguments) into a function, making it more dynamic and reusable.

//ONE PARAMETER
// function greet(name) {
//     console.log("Hello, " + name + "!");
// }

// // Calling the function with an argument
// greet("Alice");
// greet("Bob");

//MORE THAN ONE PARAMETER
// function addNumbers(a, b) {
//     return a + b;
// }

// // Calling the function with arguments
// let sum = addNumbers(5, 10);
// console.log("The sum is:", sum);

//Arrow functions (=>) provide a shorter syntax for defining functions.
//Example 1: Simple Arrow Function
// const sayHello = (name) => {
//     console.log(`Hello, ${name}!`);
// };

// // Calling the arrow function
// sayHello("Charlie");


//Example 2: Arrow Function with Implicit Return
// const multiply = (x, y) => x * y;

// console.log(multiply(4, 5)); // Output: 20


