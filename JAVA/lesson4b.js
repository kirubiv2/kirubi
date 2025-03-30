//Anonymous functions-Functions without names, they use variable names as their names
const greet= function(){
    console.log("Welcome to the world of programming.")
};

greet();

//Below is an anonymous function that invokes itself
// console.log("==============================================")

(function (){
    console.log("A function calling itself.")
})();