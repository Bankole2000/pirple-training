/*
 * File: functions.js V1.0
 * Auth: Bankole Esan
 * Desc: Pirple.com JavaScript Homework #4
 * Task: Syllogisms using Functions
 */
// function to catch any type/reference errors thrown

// Collection of men
const men = [
  { name: 'John', isMortal: true },
  { name: 'Aristotle', isMortal: true },
  { name: 'Socrates', isMortal: true },
  { name: 'Plato', isMortal: true },
];
const nameOfMan = 'Socrates'; // name of man to pass into function

const cakeFlavours = ['vanilla', 'chocolate']; // Possible flavours of cake
const cakeIsChocolate = false; // Set whether cake is chocolate or not

// Function to check if name given is among men collection
// also to return if man isMortal property - boolean
const isAMan = (name) => {
  console.log('\n====== Homework #4 ======');
  if (name && typeof name === 'string' && name.trim()) {
    name = name.trim();
    const manFound = men.find((man) => man.name === name);
    if (manFound) {
      console.table(manFound);
      console.log(`${manFound.name} is mortal: ${manFound.isMortal}`);
      return manFound.isMortal;
    } else {
      console.log(`Men Collection:`);
      console.table(men);
      console.log(`"${name}" not found in men collection`);
      return false;
    }
  } else {
    console.log('Please enter a valid Name');
    return false;
  }
};

// function to check what flavour cake is
const whatFlavor = (isChocolate, cakeFlavours) => {
  console.log('\n====== Extra Credit stuff ======');
  if (typeof isChocolate != 'boolean' || typeof cakeFlavours != 'object') {
    console.log('Please enter a boolean value as first parameter');
    console.log(`Params: ${typeof isChocolate}, ${typeof cakeFlavours}`);
    return false;
  } else {
    const params = {
      isChocolate,
      cakeFlavours,
    };
    const flavourOfCake = isChocolate ? cakeFlavours[1] : cakeFlavours[0];
    console.table(params);
    console.log(`Actual flavor of cake is: "${flavourOfCake}"`);
    return true;
  }
};

// All stuff below to catch errors
const catchError = (error, explicit) => {
  console.log(
    `[${explicit ? 'EXPLICIT' : 'INEXPLICIT'}] ${error.name}: ${error.message}`
  );
};

try {
  isAMan(nameOfMan);
} catch (e) {
  if (e instanceof TypeError) {
    catchError(e, true);
  } else {
    catchError(e, false);
  }
}

try {
  whatFlavor(cakeIsChocolate, cakeFlavours);
} catch (e) {
  if (e instanceof TypeError) {
    catchError(e, true);
  } else {
    catchError(e, false);
  }
}
