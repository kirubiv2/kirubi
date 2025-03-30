/*
Assume you have the following distance table:

Distance Table:
--------------------------------
Distance (km)   | Amount to Pay
0 - 100         | Pay 5 USD
101 - 500       | Pay 10 USD
501 - 1000      | Pay 20 USD
1001 and above  | Pay 40 USD

Task:
The students will write a JS program that uses an if-else if-else statement 
to calculate the Amount to Pay based on the distance traveled.
*/

let distance = 250; // Example distance
let amount;

if (distance >= 0 && distance <= 100) {
    amount = 5;
} else if (distance >= 101 && distance <= 500) {
    amount = 10;
} else if (distance >= 501 && distance <= 1000) {
    amount = 20;
} else if (distance >= 1001) {
    amount = 40;
} else {
    amount = "Invalid distance";
}

console.log("The amount to pay is ${amount} USD.");










//conversion of lesson 3d.py
let score = 80;
if (score >= 0 && score <= 40) {
    console.log("The student got grade E");
} else if (score > 40 && score <= 50) {
    console.log("The student got grade D");
} else if (score > 50 && score <= 60) {
    console.log("The student got grade C");
} else if (score > 60 && score <= 70) {
    console.log("The student got grade B");
} else if (score > 70 && score <= 100) {
    console.log("The student got grade A");
} else {
    console.log("Invalid Input");
}

