/*
 * File: switch.js V1.0
 * Auth: Bankole Esan
 * Desc: Pirple.com JavaScript Homework #
 * Task: Switch Statements - Time Adder function
 */

const timeAdder = (value1, label1, value2, label2) => {
  let value3, label3;
  const measure = [
    'second',
    'seconds',
    'minute',
    'minutes',
    'hour',
    'hours',
    'day',
    'days',
  ];

  const result = [];
  if (value1 <= 0 || value2 <= 0) {
    console.log(`Positive Values only`);
    return false;
  }
  if (!measure.includes(label1) || !measure.includes(label2)) {
    console.log('Invalid Time Measures');
    return false;
  }
  switch (label1) {
    case 'minute':
    case 'minutes':
      value3 = value1 + value2;
      console.log(value3, label1);
      break;

    default:
      console.log('Something wrong somewhere');
      break;
  }
};

timeAdder(2, 'minutes', 5, 'minutes');
