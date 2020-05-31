/*
 * File: variables.js V1.0
 * Auth: Bankole Esan
 * Desc: Pirple.com JavaScript Homework #1
 * Task: Differences between let, const and var.
 * Language: English
 */

/*
============================
  Hoisting
==========================

What is Hoisting? 
  Hoisiting is a Javascript mechanism where variables and function
  declarations are moved to the top of their scope before execution.
  Or, in other words, Javascripts default behaviour of moving declarations
  to the top of the execution scope.
  The word hoisting comes from the english verb - to hoist - which means to
  raise something by means of ropes and pulleys, or to just raise or haul up. 

How does Hoisting work in Javascript?
  When the javascript interpreter is executing a JS program, all function 
  and variable declarations are moved to the top of their scope regardless of 
  their actual order in the code (and without their initial values/assignments). 
  This may cause errors in runtime with variables returning undefined, because they've
  been hoisted and positioned before their actual declaration and value assignment. 
  To address this, it is recommended as best practice that programmers declare all 
  variables at the beginning of every scope. ES6 variables are not hoisted though, 
  and also, Javascript in strict mode does not allow variables to be used if they have not 
  been declared.  
*/

/*
===================================================
What are 'var', 'let', and 'const' in JavaScript?
===================================================

var: is an ES5 Javascript keyword used to declare and/or initialize
  a variable. variables declared with this keyword are
  accessible anywhere within the "current execution context" 
  scope -  i.e. Either the enclosing function scope the 
  the variable is declared in, or (if not declared within 
  a function) the global scope. They can be easily redefined, 
  redeclared and changed to other types. 
  When to use 'var': - 
  1. Use of var is generally discouraged as at ES6 release. 
  2. In an application where scoping may not be a concern or
    when declared variables need to be accessible outside of their 
    immediate block scope, but within the function scope. 

let: is an ES6 standard javascript keyword used to declare variables
  only accessible within the block scope they are initialized in
  (i.e. immediate enclosing curly bracket '{}' pair, or global if none). 
  variables declared this way can be initialized unassigned 
  (i.e. with no values), and can also be easily reassigned. 
  When to use 'let': -
  1. Use for variables whose values are required to change or be reassigned
    (e.g. counter in a for loop, boolean switch etc)
  2. Use to declare variables whose values cannot be determined as at declared
    (e.g. algebraic unknowns).
  3. Use 'let' only if you can't use const.

const: (short for constants) ES6 standard javascript keyword used to declare variables 
    which cannot be redeclared or reassigned, but whose values may 
    be transmuted/transformed. It is also block level scoped like 'let'
    variables, however, const variables cannot be declared unnassigned.
    When to use 'const': -
    1. Use for variables with known fixed values (e.g. pi, planks' constant, speed of light etc)
    2. Use for holding UI and DOM elements
    3. Use for Arrays and Objects
    4. Always use const when and were possible (recommended).
*/

/*
===================================================
    Differences between 'var', 'let', and const
===================================================
*/
console.log(`\n\t\t======== Differences between var, let and const ========`);
console.table({
  scope: {
    var: 'function or global',
    let: 'Block/Local Scope',
    const: 'Block/Local Scope',
  },
  hoisted: {
    var: true,
    let: false,
    const: false,
  },
  redeclarable: {
    var: true,
    let: true,
    const: false,
  },
  reassignable: {
    var: true,
    let: true,
    const: false,
  },
  Usage: {
    var: 'discouraged',
    let: 'if const not suited',
    const: 'recommended',
  },
  canBeUnassigned: {
    var: true,
    let: true,
    const: false,
  },
});
// Please run file with node to view differences table

/*
  =================
    Code Samples
  =================
*/

// Example 1
// An example of getting var variable to be used outside the block scope in function scope
var isValidOnce = true;
function checkIfIsValid() {
  if (isValidOnce) {
    isValidOnce = false;
    var usedOTP = 'OTP used'; // using let or const throws an error
  } else {
    isValidOnce = true;
    var newOTP = 'New OTP Generated'; // using let or const would throw an error
  }
  console.log(usedOTP || newOTP);
}
checkIfIsValid();

// Example 2
// An example of using let to declare unassigned variables
function addNumbers() {
  let x, y, sum;
  x = 5; // or some input from the user
  y = 6; // or some other input from the user
  console.log((sum = x + y));
  return sum;
}
addNumbers();

// Example 3
// An example of using const
function timeOfFlight(iniTialVelocity, projectileAngle) {
  const accDueToGravity = 9.8; // known constant value
  console.log(
    `Approx ${Math.trunc(
      (2 * iniTialVelocity * Math.sin(projectileAngle)) / accDueToGravity
    )}s assuming gravity to be a constant value of ${accDueToGravity}m/s^2`
  );
  return (2 * iniTialVelocity * Math.sin(projectileAngle)) / accDueToGravity;
}
timeOfFlight(30, 45);
