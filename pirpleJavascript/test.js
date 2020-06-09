// // console.log('Hello world');

// // const arr1 = [1, 2, 3];
// // const arr2 = [1, 2, 3];
// // const arr3 = ['1', '2', '3'];

// // console.log(arr1 == arr2);
// // console.log(arr1 !== arr2);
// // console.log(arr1 === arr2);
// // console.log(arr1[0] === arr2[0]
// //   && arr1[1] === arr2[1]
// //   && arr1[2] === arr2[2]);
// // console.log(arr1[0] == arr3[0]);
// // // What's the output?

// // const cake = 'vanilla' || 'chocolate';
// // console.log(cake);

// const myFruit = 'orange';

// switch (myFruit) {
//   case 'apple':
//     console.log('Great! I love apples.');
//     break;
//   case 'orange':
//     console.log('Good choice - Oranges');
//     break;
//   case 'banana':
//     console.log('OK - Nice Banana');
//     break;
//   default:
//     console.log("I didn't understand that but sure");
//     break;
// }

// try {
//   // some usless code I'm trying to run
//   console.log("the code ran mf 😎 - line 38")
// }
// catch(err) {
//   console.warn("Dude, You really F*d up time this time 😕😝 - line 41", err);
// }

// While loop
// const names = [
//   'John',
//   'James',
//   'Joe',
//   'Mary',
//   'Micheal',
//   'Joseph',
//   'Natalia',
//   'Chris',
// ];

// const nameLooper = (arr, userName) => {
//   let index = 0;
//   while (index < arr.length) {
//     if (arr[index] === userName) {
//       console.log(`${userName} is ${arr.indexOf(userName)}`);
//       break;
//     }
//     console.log(arr[index]);
//     index += 1;
//   }
// };

// nameLooper(names, 'Chris');

// // Do while - code should run at least one
// let shouldRunOnlyOnce = false;

// do {
//   console.log('looping!');
//   shouldRunOnlyOnce = false;
// } while (shouldRunOnlyOnce);

// // Labels
// outerLoop: for (let i = 0; i < 10; i++) {
//   console.log('loop #' + i);
//   innerLoop: for (let a = 0; a < 10; a++) {
//     console.log('inner loop #' + a);
//     if (a === 3) {
//       break innerLoop;
//     }
//     if (i === 5) {
//       break outerLoop;
//     }
//   }
// }
// console.log('Finished Loop');
// const looper = (value) => {
//   setInterval(() => {
//     console.log(value);
//   }, 1000);
// };

// for (let i = 0; i < 10; i++) {
//   looper(i);
// }

// // usng es 6
// for (let i = 0; i < 10; i++) {
//   setTimeout(() => {
//     console.log(i);
//   }, i * 500);

// }

// let userInput = prompt('Enter something: ');
// console.log(userInput);

// const users = { 1: 'sally', 2: 'Billy', 3: 'Ashley', 4: 'timmy' };
// //  for in loop - good for objects
// for (let prop in users) {
//   console.log(prop); // return keys
//   console.log(users[prop]); // return values of keys
// }

// for of loop - can break can continue

const originalArray = ['Chris', 'Chris', 'Jane', 'Sally', 'Billy'];

const uniqueSet = new Set(originalArray);
for (const n of uniqueSet) {
  console.log(n, uniqueSet);
  if (n === 'Chris') {
    break;
  }
}
