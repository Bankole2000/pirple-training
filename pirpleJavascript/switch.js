/*
 * File: switch.js V1.0
 * Auth: Bankole Esan
 * Desc: Pirple.com JavaScript Homework #5
 * Task: Switch Statements - Time Adder function
 */

//  Variables for the time adder function
const value1 = 48; // int - must be whole number > 0
const label1 = 'hours'; // string - must be time measure (Hours minures, etc)
const value2 = 3;
const label2 = 'days';

// Time Adder function itself
const timeAdder = (value1, label1, value2, label2) => {
  let value3, // Sum of value1 and value2 after label computation
    unifiedLabel, // unified label for eventual output
    result = []; // for storing result to present to user

  // time measures for validation / Sanitation
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

  // Sanity Checks
  if (!Number.isInteger(value1) || !Number.isInteger(value2)) {
    console.log('Please enter only valid numerical values for time - line 34');
    return false;
  }
  if (value1 <= 0 || value2 <= 0) {
    console.log(`Positive Values only`);
    return false;
  }
  if (!measure.includes(label1) || !measure.includes(label2)) {
    console.log('Invalid Time Measures - line 42');
    return false;
  }
  if (
    isNumericallyValid(value1, label1) &&
    isNumericallyValid(value2, label2)
  ) {
    if (label1 === label2) {
      unifiedLabel = label1;
      // if labels the same, go ahead to switch statement for addition and normalization
    } else {
      // change labels to smiliar unit (seconds)
      const data1 = reduceToSeconds(value1, label1);
      console.log('To be Added to ');
      const data2 = reduceToSeconds(value2, label2);
      unifiedLabel = 'seconds';
      value1 = data1[0];
      value2 = data2[0];
    }
  } else {
    console.log(
      'Use singular labels for unitary values and Pluralized labels for values > 1 - line 62'
    );
    return false;
  }
  // End of Sanity checks

  // In Each case, add, then recursively normalize
  switch (unifiedLabel) {
    case 'second':
    case 'seconds':
      value3 = value1 + value2;
      if (value3 >= 60) {
        console.log(`Normalizing ${value3} in ${unifiedLabel}  - line 74`);
        result = normalize(value3, unifiedLabel);
      } else {
        console.log(value3, unifiedLabel, ' - Line 77');
        result = [value3, unifiedLabel];
      }
      break;
    case 'minute':
    case 'minutes':
      value3 = value1 + value2;
      if (value3 >= 60) {
        console.log(`Normalizing ${value3} in ${unifiedLabel}  - line 85`);
        result = normalize(value3, unifiedLabel);
      } else {
        console.log(value3, unifiedLabel, ' - Line 88');
        result = [value3, unifiedLabel];
      }
      break;
    case 'hour':
    case 'hours':
      value3 = value1 + value2;
      if (value3 >= 24) {
        console.log(`Normalizing ${value3} in ${unifiedLabel}  - line 96`);
        result = normalize(value3, unifiedLabel);
      } else {
        console.log(value3, unifiedLabel, ' - Line 99');
        result = [value3, unifiedLabel];
      }
      break;
    case 'day':
    case 'days':
      value3 = value1 + value2;
      result = [value3, unifiedLabel];
      break;
  }
  console.log(result, ' - line 109');
  return result;
};

// Normalize function to recursively set value to highest time measure
const normalize = (value, label) => {
  let newValue, newLabel, result;
  switch (label) {
    case 'second':
    case 'seconds':
      newValue = Math.floor(value / 60);
      newLabel = 'minutes';
      if (newValue >= 60) {
        console.log(`Normalizing ${newValue} in ${newLabel}  - line 122`);
        return normalize(newValue, newLabel);
      }
      result = [newValue, newLabel];
      break;
    case 'minute':
    case 'minutes':
      newValue = Math.floor(value / 60);
      newLabel = 'hours';
      if (newValue >= 24) {
        console.log(`Normalizing ${newValue} in ${newLabel}  - line 132`);
        return normalize(newValue, newLabel);
      }
      result = [newValue, newLabel];
      break;
    case 'hour':
    case 'hours':
      newValue = Math.floor(value / 24);
      newLabel = 'days';
      if (newValue >= 24) {
        console.log(`Normalizing ${newValue} in ${newLabel}  - line 142`);
        return normalize(newValue, newLabel);
      }
      result = [newValue, newLabel];
      break;
    case 'day':
    case 'days':
      newValue = value;
      newLabel = 'days';
      result = [newValue, newLabel];
      return result;
      break;
    default:
      break;
  }
  result[0] === 1
    ? (result[1] = result[1].substring(0, result[1].length - 1))
    : '';
  return result;
};

// Check plurality of value and label
const isNumericallyValid = (value, label) => {
  const singularMeasure = ['second', 'minute', 'hour', 'day'];
  const pluralMeasure = ['seconds', 'minutes', 'hours', 'days'];
  if (value === 1 && singularMeasure.includes(label)) {
    return true;
  } else if (value > 1 && pluralMeasure.includes(label)) {
    return true;
  } else {
    return false;
  }
};

// Reduce different labels to seconds then add and normalize
const reduceToSeconds = (value, label) => {
  switch (label) {
    case 'minute':
    case 'minutes':
      value *= 60;
      break;

    case 'hour':
    case 'hours':
      value *= 3600;
      break;

    case 'day':
    case 'days':
      value *= 86400;
      break;

    default:
      value;
      break;
  }
  console.log(value, 'in seconds - line 198');
  return [value, 'seconds'];
};

timeAdder(value1, label1, value2, label2);
