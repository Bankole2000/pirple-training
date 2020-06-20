/*
 * File: index.js
 * Auth: Bankole Esan
 * Desc: Pirple.com NodeJS Homework #1
 * Task: RESTful JSON API
 */

//  Dependencies
const _data = require('./data');
const helpers = require('./helpers');

// SECTION: DESCRIPTION: Requests Handlers that return to OBJECT: router in FILE: index.js
const handlers = {};

// FUNCTION: @ROUTE '/users'
handlers.users = (data, callback) => {
  const acceptableMethods = ['POST', 'GET', 'PUT', 'DELTE'];
  if (acceptableMethods.indexOf(data.method) > -1) {
    handlers._users[data.method](data, callback);
  } else {
    callback(405);
  }
};

// CONTAINER: for user submethods
handlers._users = {};

// @POST CREATE: New User
// @DATA - firstname, lastname, phone, password, and tosAgreement
// @OPTIONAL - None
handlers._users.POST = (data, callback) => {
  // Check that all required fields are filld out
  const firstName =
    typeof data.payload.firstName == 'string' &&
    data.payload.firstName.trim().length > 0
      ? data.payload.firstName.trim()
      : false;
  const lastName =
    typeof data.payload.lastName == 'string' &&
    data.payload.lastName.trim().length > 0
      ? data.payload.lastName.trim()
      : false;
  const phone =
    typeof data.payload.phone == 'string' &&
    data.payload.phone.trim().length == 11
      ? data.payload.phone.trim()
      : false;
  const password =
    typeof data.payload.password == 'string' &&
    data.payload.password.trim().length > 0
      ? data.payload.password.trim()
      : false;
  const tosAgreement =
    typeof data.payload.tosAgreement == 'boolean' &&
    data.payload.tosAgreement == true
      ? true
      : false;

  if (firstName && lastName && phone && password && tosAgreement) {
    // subFunction: Make sure user does not already exist
    _data.read('users', phone, (err, data) => {
      if (err) {
        // i.e. the user doesn't exist
        // subFunction: Hash the password
        const hashedPassword = helpers.hash(password);

        // subFunction: create the user Object
        if (hashedPassword) {
          const userObject = {
            firstName,
            lastName,
            phone,
            hashedPassword,
            tosAgreement: true,
          };

          // STORE: the user data
          _data.create('users', phone, userObject, (err) => {
            if (!err) {
              callback(200);
            } else {
              console.log(err);
              callback(500, { Error: 'Could not create the new user' });
            }
          });
        } else {
          callback(500, { Error: "Could not Hash the users's password" });
        }
      } else {
        callback(400, {
          Error: 'A user with that phone number already exists',
        });
      }
    });
  } else {
    callback(400, { Error: 'Missing required Fields', data: data });
  }
};

// @GET READ: Get user data
// @DATA - phone
handlers._users.GET = (data, callback) => {};
handlers._users.PUT = (data, callback) => {};
handlers._users.DELETE = (data, callback) => {};

// endOfContainer: handler._users

// FUNCTION: @ROUTE  '/ping'
handlers.ping = (data, callback) => {
  callback(200);
};
// FUNCTION: @ROUTE  '404'
handlers.notFound = (data, callback) => {
  callback(404, {
    error: true,
    message: "This Route doesn't exist! i.e. Not Found",
  });
};
// FUNCTION: @ROUTE  '/sample'
handlers.sample = (data, callback) => {
  callback(406, { error: false, name: 'sample Handler' });
};
// FUNCTION: @ROUTE  '/hello'
handlers.hello = (data, callback) => {
  callback(200, {
    error: false,
    message: 'Welcome to the Node JS Master Class',
  });
}; // endOfSection:

module.exports = handlers;
