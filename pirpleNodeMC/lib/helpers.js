/*
 * File: index.js
 * Auth: Bankole Esan
 * Desc: Pirple.com NodeJS Homework #1
 * Task: RESTful JSON API
 */

// Dependencies
const crypto = require('crypto');
const config = require('./config');

//  SECTION: DESCRIPTION: Helpers for various tasks
// CONTAINER:
const helpers = {};

// Create a SHA256 has
helpers.hash = (str) => {
  if (typeof str == 'string' && str.length > 0) {
    const hash = crypto
      .createHmac('sha256', config.hashingSecret)
      .update(str)
      .digest('hex');
    return hash;
  } else {
    return false;
  }
};

// FUNCTION: Parse a JSON string to an object in all cases, without throwing an error
helpers.parseJsonToObject = (str) => {
  try {
    const obj = JSON.parse(str);
    return obj;
  } catch (e) {
    console.log(e);
    return {};
  }
};

// Create a string of random alphanumeric characters, of a given length
helpers.createRandomString = (strLength) => {
  strLength = typeof strLength == 'number' && strLength > 0 ? strLength : false;
  if (strLength) {
    // define all possible characters that could go into a string
    const possibleCharacters = 'abcdefghijklmnopqrstuvwxyz0123456789';

    // Start the final string
    let str = '';
    for (i = 1; i <= strLength; i++) {
      // Get a random character and append to final string
      const randomCharacter = possibleCharacters.charAt(
        Math.floor(Math.random() * possibleCharacters.length)
      );
      str += randomCharacter;
    }
    return str;
  } else {
    return false;
  }
};

// Export the module
module.exports = helpers;
