/*
 * FileName: ifStatements.js V1.0
 * Author: Bankole Esan
 * Description: Pirple.com JavaScript Homework #3
 * Task: Syllogisms using logical operators
 */

//  Set Premise as params
const manToFind = 'Socrates'; // Set name of person to search for 🤵
const allMenAreMortal = true; // Grant all men eternal life if you wish 👼 🙏
allMenAreMortal
  ? console.log(`\nYou made all men MORTAL`)
  : console.log(`\nYou made all men IMMORTAL`);

// ============= Possible Solution 1 ================
//  collection of items called men
// A man named 'Socrates' is one of them
const men = [
  { name: 'John' },
  { name: 'Aristotle' },
  { name: 'Socrates' },
  { name: 'Plato' },
];

// Grant all men the mortality status the gods wish
men.forEach((man) => {
  man.isMortal = allMenAreMortal;
});

// Function to check if someone is a man
const isAMan = (name) => {
  const isAMan = men.find((man) => man.name === name) ? true : false;
  return isAMan;
};

console.log('\n======== Solution 1 ==========');

console.table(men);
if (isAMan(manToFind)) {
  const manFound = men.find((man) => man.name === manToFind);
  console.log(`${manFound.name} is a man therefore`);
  console.log(
    `${manFound.name} is Mortal: ${manFound ? manFound.isMortal : ''}`
  );
} else {
  console.log(`All hail the immortal ${manToFind}`);
  console.log(`${manToFind} is Not a man and therefore probably immortal`);
}
// =============== End of Possible Solution 1 ===============

// ============= Possible Solution 2 ================
// Socrates is part of a collection of men
const menCollection = ['John', 'Aristotle', 'Socrates', 'Plato'];

console.log('\n======== Solution 1 ==========');
console.log(`Men's Collection : [${menCollection}]`);
console.log(`The gods set all men's mortality to: ${allMenAreMortal}`);

if (menCollection.includes(manToFind) && allMenAreMortal) {
  console.log(
    `Since ${manToFind} is in ${menCollection}\n${manToFind} is therefore mortal`
  );
} else if (menCollection.includes(manToFind) && !allMenAreMortal) {
  console.log(`Death took a break so \n${manToFind} is immortal now`);
} else if (!menCollection.includes(manToFind)) {
  console.log(
    `${manToFind} is not in [${menCollection}] so we can't tell if he's Immortal or not`
  );
}
// ============= End of Possible Solution 2 ================

// ============== Extra Credit Stuff ==================
let flavour1 = 'vanilla',
  flavour2 = 'chocolate';
const cake = flavour2;

console.log('\n======== Extra Credit ==========');

if (cake === flavour1 || cake === flavour2) {
  console.log(`This cake is either ${flavour1} or ${flavour2}`);
}
if (cake !== flavour1) {
  console.log(`This cake is not ${flavour1}`);
  console.log(`Therefore this cake is ${flavour2}`);
} else {
  console.log(`This cake is not ${flavour2}`);
  console.log(`Therefore this cake is ${flavour1}`);
}
