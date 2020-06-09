/*
 * File: fizzbuzzprime.js V1.0
 * Auth: Bankole Esan
 * Desc: Pirple.com JavaScript Homework #6
 * Task: fizz buzz prime
 */

//  set variables
const fizz = 'Fizz';
const buzz = 'Buzz';
const prime = 'Prime';

const isPrimeNumber = (arg) => {
  if (arg >= 2) {
    for (let i = 2; i < arg; i++) {
      if (arg % i == 0) {
        return false;
      }
    }
  } else {
    return false;
  }
  return true;
};

let i = 1;
do {
  if (isPrimeNumber(i)) {
    console.log(prime);
    i++;
    continue;
  }
  if (i % 3 == 0 && i % 5 == 0) {
    console.log(`${fizz}${buzz}`);
    i++;
    continue;
  }
  if (i % 3 == 0) {
    console.log(fizz);
    i++;
    continue;
  }
  if (i % 5 == 0) {
    console.log(buzz);
    i++;
    continue;
  }
  console.log(i);
  i++;
} while (i < 100);
