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

// Export the module
module.exports = helpers;
