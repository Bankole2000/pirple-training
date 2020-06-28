/*
 * File: index.js
 * Auth: Bankole Esan12345678911
 * Desc: Pirple.com NodeJS Homework #1
 * Task: RESTful JSON API
 */

//  Dependencies
const _data = require('./data');
const helpers = require('./helpers');
const config = require('./config');

// SECTION: DESCRIPTION: Requests Handlers that return to OBJECT: router in FILE: index.js
const handlers = {};

//#region - @ROUTE'/users' handlers
// FUNCTION: @ROUTE '/users'
handlers.users = (data, callback) => {
  const acceptableMethods = ['POST', 'GET', 'PUT', 'DELETE'];
  if (acceptableMethods.indexOf(data.method) > -1) {
    handlers._users[data.method](data, callback);
  } else {
    callback(405);
  }
};
handlers._users = {};

// @POST CREATE: New User
// @DATA - firstname, lastname, phone, password, and tosAgreement - req Body
// PUBLIC: - anyone can register
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
// @DATA - phone - url query string
// @OPTIONAL - None
// @ROUTE is PRIVATE: - only for authenticated users
handlers._users.GET = (data, callback) => {
  // TODO: only let authenticated users access their object

  const phone =
    typeof data.queryStringObject.phone == 'string' &&
    data.queryStringObject.phone.trim().length == 11
      ? data.queryStringObject.phone.trim()
      : false;

  if (phone) {
    // Get the token from the headers
    const token =
      typeof data.headers.token == 'string' ? data.headers.token : false;
    // Verify that the token is valid for the phone number
    handlers._tokens.verifyToken(token, phone, (tokenIsValid) => {
      if (tokenIsValid) {
        // STORE: READ: Lookup the user
        _data.read('users', phone, (err, data) => {
          if (!err && data) {
            // remove the hashed password before sending
            delete data.hashedPassword;
            callback(200, data);
          } else {
            callback(404, { Error: 'That user does not exist' });
          }
        });
      } else {
        callback(403, {
          Error: 'Missing required token in header, or token is invalid',
        });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};

// @GET UPDATE: Get user data
// @DATA - phone - req body
// @OPTIONAL - firstName, lastName, password
// PRIVATE: - only for authenticated users
// TODO: Only let user update own object
handlers._users.PUT = (data, callback) => {
  // REQUIRED: Phone is required field
  const phone =
    typeof data.payload.phone == 'string' &&
    data.payload.phone.trim().length == 11
      ? data.payload.phone.trim()
      : false;
  // OPTIONAL: Other fields are optional
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
  const password =
    typeof data.payload.password == 'string' &&
    data.payload.password.trim().length > 0
      ? data.payload.password.trim()
      : false;
  // Error if phone is invalid
  if (phone) {
    // Error if nothing else is sent
    if (firstName || lastName || password) {
      // Get the token from the headers
      const token =
        typeof data.headers.token == 'string' ? data.headers.token : false;
      // Verify that the token is valid for the phone number
      handlers._tokens.verifyToken(token, phone, (tokenIsValid) => {
        if (tokenIsValid) {
          // Lookup the user
          _data.read('users', phone, (err, userData) => {
            if (!err && userData) {
              // update the fields necessary
              if (firstName) {
                userData.firstName = firstName;
              }
              if (lastName) {
                userData.lastName = lastName;
              }
              if (password) {
                userData.password = password;
              }
              // STORE: store user data
              _data.update('users', phone, userData, (err) => {
                if (!err) {
                  callback(200, { Message: 'Successfully Updated the user' });
                } else {
                  console.log(err);
                  callback(500, { Error: 'Could not update the user' });
                }
              });
            } else {
              callback(404, { Error: "Couldn't Find the specified user" });
            }
          });
        } else {
          callback(403, { Error: 'Invalid token' });
        }
      });
    } else {
      callback(400, { Error: 'Missing fields to update' });
    }
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};

// @DELETE Delete user data
// @DATA - phone - req body
// @OPTIONAL - firstName, lastName, password
// PRIVATE: - only for authenticated users
// TODO: Only let user delete own object
handlers._users.DELETE = (data, callback) => {
  // TODO: only let authenticated users access their object
  const phone =
    typeof data.queryStringObject.phone == 'string' &&
    data.queryStringObject.phone.trim().length == 11
      ? data.queryStringObject.phone.trim()
      : false;

  if (phone) {
    // Get the token from the headers
    const token =
      typeof data.headers.token == 'string' ? data.headers.token : false;
    // Verify that the token is valid for the phone number
    handlers._tokens.verifyToken(token, phone, (tokenIsValid) => {
      if (tokenIsValid) {
        // STORE: DEL: Lookup the user
        _data.read('users', phone, (err, userData) => {
          if (!err && userData) {
            _data.delete('users', phone, (err) => {
              if (!err) {
                // NOTE: When you delete the user you have to delete all the user related data
                const userChecks =
                  typeof userData.checks == 'object' &&
                  userData.checks instanceof Array
                    ? userData.checks
                    : [];
                const checksToDelete = userChecks.length;
                if (checksToDelete > 0) {
                  let checksDeleted = 0;
                  let deletionErrors = false;
                  // Loop through the checks and delete
                  userChecks.forEach((checkId) => {
                    _data.delete('checks', checkId, (err) => {
                      if (err) {
                        deletionErrors = true;
                      }
                      checksDeleted++;
                      if (checksDeleted == checksToDelete) {
                        if (!deletionErrors) {
                          callback(200, {
                            Message: 'All user checks successfully deleted',
                          });
                        } else {
                          callback(500, {
                            Errors:
                              'Errors encountered while trying to delete all the users checks',
                          });
                        }
                      }
                    });
                  });
                } else {
                  callback(200, { Message: 'User successfully deleted' });
                }
              } else {
                callback(500, { Error: 'Could not delete the specified user' });
              }
            });
          } else {
            callback(404, { Error: 'Could not find specified user' });
          }
        });
      } else {
        callback(403, { Error: 'Missing or token is invalid' });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};
//#endregion

//#region - @ROUTE '/tokens'
handlers.tokens = (data, callback) => {
  const acceptableMethods = ['POST', 'GET', 'PUT', 'DELETE'];
  if (acceptableMethods.indexOf(data.method) > -1) {
    handlers._tokens[data.method](data, callback);
  } else {
    callback(405);
  }
};
handlers._tokens = {};

// @GET READ: Get user data from token
// @DATA - id - url query string
// @OPTIONAL - None
// PRIVATE: - only for authenticated users
handlers._tokens.GET = (data, callback) => {
  // TODO: only let authenticated users access their object
  const id =
    typeof data.queryStringObject.id == 'string' &&
    data.queryStringObject.id.trim().length == 20
      ? data.queryStringObject.id.trim()
      : false;

  if (id) {
    // STORE: READ: Lookup the token
    _data.read('tokens', id, (err, tokenData) => {
      if (!err && tokenData) {
        callback(200, tokenData);
      } else {
        callback(404, { Error: 'That user does not exist' });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};

// @POST CREATE: New Token for user
// @DATA - phone, password - req body
// PUBLIC: - registered users can login
// @OPTIONAL - None
handlers._tokens.POST = (data, callback) => {
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
  if (phone && password) {
    // STORE: READ: Lookup user who matches that phone number
    _data.read('users', phone, (err, userData) => {
      if (!err && userData) {
        // hash the sent password and compare to stored password
        const hashedPassword = helpers.hash(password);
        if (hashedPassword === userData.hashedPassword) {
          // If Valid create a new token with a random name, set expiration date 1 hour into the future
          const tokenId = helpers.createRandomString(20);
          const expires = Date.now() + 1000 * 60 * 60;
          const tokenObject = {
            phone,
            id: tokenId,
            expires,
          };

          // STORE: CREATE: store the token id
          _data.create('tokens', tokenId, tokenObject, (err) => {
            if (!err) {
              callback(200, {
                Message: 'Token Successfully created',
                tokenObject,
              });
            } else {
              callback(500, { Error: 'Could not create the new token' });
            }
          });
        } else {
          callback(400, {
            Error: 'Password did not match the specified users stored password',
          });
        }
      } else {
        callback(400, { Error: 'Could not find the specified user' });
      }
    });
  } else {
    callback(400, { Error: 'Missing required Fields' });
  }
};

// @GET UPDATE: update user token
// @DATA - id, extend - req body
// @OPTIONAL -
// PRIVATE: - only for authenticated users
// TODO: Only logged in user to extend token by 1 hour
handlers._tokens.PUT = (data, callback) => {
  const id =
    typeof data.payload.id == 'string' && data.payload.id.trim().length > 0
      ? data.payload.id.trim()
      : false;
  const extend =
    typeof data.payload.extend == 'boolean' && data.payload.extend == true
      ? true
      : false;

  if (id && extend) {
    // STORE: READ: lookup the token
    _data.read('tokens', id, (err, tokenData) => {
      if (!err && tokenData) {
        // Check to make sure the token isn't already expired
        if (tokenData.expires > Date.now()) {
          // Set the expiration an hour from now
          tokenData.expires = Date.now() + 1000 * 60 * 60;

          // STORE: UPDATE: update the token with new expires information
          _data.update('tokens', id, tokenData, (err) => {
            if (!err) {
              callback(200, {
                Message: 'Success. Token successfully extended',
              });
            } else {
              callback(500, {
                Error: "Could not update the token's expiration",
              });
            }
          });
        } else {
          callback(400, {
            Error: 'The token has already expired, and cannot be extended',
          });
        }
      } else {
        callback(400, { Error: 'Specified token does not exist' });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields or fields are invalid' });
  }
};

// @DELETE Delete user token
// @DATA - id - queryString
// @OPTIONAL - none
// PRIVATE: - only for authenticated users
// TODO: Only let user delete own object
handlers._tokens.DELETE = (data, callback) => {
  // TODO: only let authenticated users access their object
  const id =
    typeof data.queryStringObject.id == 'string' &&
    data.queryStringObject.id.trim().length == 20
      ? data.queryStringObject.id.trim()
      : false;

  if (id) {
    // STORE: DEL: Lookup the user
    _data.read('tokens', id, (err, tokenData) => {
      if (!err && tokenData) {
        _data.delete('tokens', id, (err) => {
          if (!err) {
            callback(200, { Message: 'User token successfully deleted' });
          } else {
            callback(500, {
              Error: 'Could not delete the specified user token',
            });
          }
        });
      } else {
        callback(404, { Error: 'Could not find specified token' });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};
//#endregion

//#region - @ROUTE '/checks'
handlers.checks = (data, callback) => {
  const acceptableMethods = ['POST', 'GET', 'PUT', 'DELETE'];
  if (acceptableMethods.indexOf(data.method) > -1) {
    handlers._checks[data.method](data, callback);
  } else {
    callback(405);
  }
};
handlers._checks = {};

// @POST CREATE: New Check
// @DATA - protocol, url, method, successCodes, timeoutSeconds - req Body
// PRIVATE: - requires token in header
// @OPTIONAL - None
handlers._checks.POST = (data, callback) => {
  // validate inputs
  const protocol =
    typeof data.payload.protocol == 'string' &&
    ['https', 'http'].indexOf(data.payload.protocol) > -1
      ? data.payload.protocol
      : false;
  const url =
    typeof data.payload.url == 'string' && data.payload.url.trim().length > 0
      ? data.payload.url.trim()
      : false;
  const method =
    typeof data.payload.method == 'string' &&
    ['get', 'post', 'put', 'delete'].indexOf(data.payload.method) > -1
      ? data.payload.method
      : false;
  const successCodes =
    typeof data.payload.successCodes == 'object' &&
    data.payload.successCodes instanceof Array &&
    data.payload.successCodes.length > 0
      ? data.payload.successCodes
      : false;
  const timeoutSeconds =
    typeof data.payload.timeoutSeconds == 'number' &&
    data.payload.timeoutSeconds % 1 === 0 &&
    data.payload.timeoutSeconds >= 1 &&
    data.payload.timeoutSeconds <= 5
      ? data.payload.timeoutSeconds
      : false;

  if (protocol && url && method && successCodes && timeoutSeconds) {
    // Get token from the header
    const token =
      typeof data.headers.token == 'string' ? data.headers.token : false;

    // STORE: READ: lookup token
    _data.read('tokens', token, (err, tokenData) => {
      if (!err && tokenData) {
        const userPhone = tokenData.phone;

        // STORE: READ: Lookup the user data
        _data.read('users', userPhone, (err, userData) => {
          if (!err && userData) {
            const userChecks =
              typeof userData.checks == 'object' &&
              userData.checks instanceof Array
                ? userData.checks
                : [];
            if (userChecks.length < config.maxChecks) {
              // Create a random Id for the check
              const checkId = helpers.createRandomString(20);
              // Create the check object and include the userphone
              const checkObject = {
                checkId,
                userPhone,
                protocol,
                url,
                method,
                successCodes,
                timeoutSeconds,
              };

              // STORE: CREATE: new check save to disk
              _data.create('checks', checkId, checkObject, (err) => {
                if (!err) {
                  // Add the check Id to the user's object
                  userData.checks = userChecks;
                  userData.checks.push(checkId);
                  // STORE: UPDATE:
                  _data.update('users', userPhone, userData, (err) => {
                    if (!err) {
                      callback(200, {
                        Message: 'New Check created',
                        checkObject,
                      });
                    } else {
                      callback(500, {
                        Error: 'Could not update the user with the new check',
                        err,
                      });
                    }
                  });
                } else {
                  callback(500, { Error: 'Could not create the new check' });
                }
              });
            } else {
              callback(400, {
                Error: `The user already has the maximum number of checks (${config.maxChecks})`,
                userData,
              });
            }
          } else {
            callback(403, { Error: 'No user with that token exists' });
          }
        });
      } else {
        callback(403, {
          Error: 'Missing required token or token invalid',
          err,
        });
      }
    });
  } else {
    callback(400, {
      Error: 'Missing required fields, or inputs are invalid',
      protocol,
      url,
      method,
      successCodes,
      timeoutSeconds,
    });
  }
};

// @GET READ: View Check details
// @DATA - checkId - req Body
// PRIVATE: - requires token in header
// @OPTIONAL - None
handlers._checks.GET = (data, callback) => {
  // TODO: only let authenticated users access their object

  const checkId =
    typeof data.queryStringObject.checkId == 'string' &&
    data.queryStringObject.checkId.trim().length == 20
      ? data.queryStringObject.checkId.trim()
      : false;

  if (checkId) {
    // STORE: READ: Check for the checkId in storage
    _data.read('checks', checkId, (err, checkData) => {
      if (!err && checkData) {
        // Get the token from the headers
        const token =
          typeof data.headers.token == 'string' ? data.headers.token : false;
        // Verify that the token is valid for the phone number
        handlers._tokens.verifyToken(
          token,
          checkData.userPhone,
          (tokenIsValid) => {
            if (tokenIsValid) {
              // Return the check Data
              callback(200, checkData);
            } else {
              callback(403, {
                Error: 'Missing required token in header, or token is invalid',
              });
            }
          }
        );
      } else {
        callback(404, { Error: 'Check with that checkId not found', err });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};

// @PUT UPDATE: New User
// @DATA - checkId - req Body
// PRIVATE: - requires user token in header
// @OPTIONAL - protocol, url, method, successCodes, timeoutSeconds
handlers._checks.PUT = (data, callback) => {
  // REQUIRED: inputs
  const checkId =
    typeof data.payload.checkId == 'string' &&
    data.payload.checkId.trim().length == 20
      ? data.payload.checkId.trim()
      : false;

  // OPTIONAL:
  const protocol =
    typeof data.payload.protocol == 'string' &&
    ['https', 'http'].indexOf(data.payload.protocol) > -1
      ? data.payload.protocol
      : false;
  const url =
    typeof data.payload.url == 'string' && data.payload.url.trim().length > 0
      ? data.payload.url.trim()
      : false;
  const method =
    typeof data.payload.method == 'string' &&
    ['get', 'post', 'put', 'delete'].indexOf(data.payload.method) > -1
      ? data.payload.method
      : false;
  const successCodes =
    typeof data.payload.successCodes == 'object' &&
    data.payload.successCodes instanceof Array &&
    data.payload.successCodes.length > 0
      ? data.payload.successCodes
      : false;
  const timeoutSeconds =
    typeof data.payload.timeoutSeconds == 'number' &&
    data.payload.timeoutSeconds % 1 === 0 &&
    data.payload.timeoutSeconds >= 1 &&
    data.payload.timeoutSeconds <= 5
      ? data.payload.timeoutSeconds
      : false;

  if (checkId) {
    if (protocol || url || method || successCodes || timeoutSeconds) {
      // STORE: READ:
      _data.read('checks', checkId, (err, checkData) => {
        if (!err && checkData) {
          // Get the token from the headers
          const token =
            typeof data.headers.token == 'string' ? data.headers.token : false;
          // Verify that the token is valid for the phone number
          handlers._tokens.verifyToken(
            token,
            checkData.userPhone,
            (tokenIsValid) => {
              if (tokenIsValid) {
                // Update the check where Necessary
                if (protocol) {
                  checkData.protocol = protocol;
                }
                if (url) {
                  checkData.url = url;
                }
                if (method) {
                  checkData.method = method;
                }
                if (successCodes) {
                  checkData.successCodes = successCodes;
                }
                if (timeoutSeconds) {
                  checkData.timeoutSeconds = timeoutSeconds;
                }
                // STORE: UPDATE:
                _data.update('checks', checkId, checkData, (err) => {
                  if (!err) {
                    callback(200, {
                      Message: 'Check successfully updated',
                      checkData,
                    });
                  } else {
                    callback(500, {
                      Error: 'Could not update check data',
                      err,
                    });
                  }
                });
              } else {
                callback(403, {
                  Error:
                    'Missing required token in header, or token is invalid',
                });
              }
            }
          );
        } else {
          callback(400, { Error: 'Check ID did not exist' });
        }
      });
    } else {
      callback(400, { Error: 'Missing fields to update' });
    }
  } else {
    callback(400, { Error: 'Missing required field', payload: data.payload });
  }
};

// @DELETE DELETE: New User
// @DATA - checkId - Query Params
// PRIVATE: - requires user token in header
// @OPTIONAL - None
handlers._checks.DELETE = (data, callback) => {
  // TODO: only let authenticated users access their object
  const checkId =
    typeof data.queryStringObject.checkId == 'string' &&
    data.queryStringObject.checkId.trim().length == 20
      ? data.queryStringObject.checkId.trim()
      : false;

  if (checkId) {
    // STORE: READ: Look up the Check ID
    _data.read('checks', checkId, (err, checkData) => {
      if (!err && checkData) {
        // Get the token from the headers
        const token =
          typeof data.headers.token == 'string' ? data.headers.token : false;
        // Verify that the token is valid for the phone number
        handlers._tokens.verifyToken(
          token,
          checkData.userPhone,
          (tokenIsValid) => {
            if (tokenIsValid) {
              // STORE: DELETE: Delete the CheckData from storage
              _data.delete('checks', checkId, (err) => {
                if (!err) {
                  // STORE: DEL: Lookup the user
                  _data.read('users', checkData.userPhone, (err, userData) => {
                    if (!err && userData) {
                      const userChecks =
                        typeof userData.checks == 'object' &&
                        userData.checks instanceof Array
                          ? userData.checks
                          : [];
                      const checkPosition = userChecks.indexOf(checkId);
                      if (checkPosition > -1) {
                        userChecks.splice(checkPosition, 1);
                        _data.update(
                          'users',
                          checkData.userPhone,
                          userData,
                          (err) => {
                            if (!err) {
                              callback(200, {
                                Message: 'User successfully updated',
                              });
                            } else {
                              callback(500, {
                                Error:
                                  'Could not update the checks of the specified user',
                              });
                            }
                          }
                        );
                      } else {
                        callback(500, {
                          Error: 'Could not find the check on the users object',
                        });
                      }
                    } else {
                      callback(500, {
                        Error:
                          'Could not find the specified user with the Check',
                      });
                    }
                  });
                } else {
                  callback(500, {
                    Error: 'Could not delete the specified check',
                  });
                }
              });
            } else {
              callback(403, { Error: 'Missing or token is invalid' });
            }
          }
        );
      } else {
        callback(400, { Error: 'This check with that id was not found' });
      }
    });
  } else {
    callback(400, { Error: 'Missing required fields' });
  }
};
//#endregion

// FUNCTION: Verify if a given token_id is currently valid for a given user
handlers._tokens.verifyToken = (id, phone, callback) => {
  // STORE: READ: Lookup the token
  _data.read('tokens', id, (err, tokenData) => {
    if (!err && tokenData) {
      // CHeck that the token is for the given user and has not expired
      if (tokenData.phone == phone && tokenData.expires > Date.now()) {
        callback(true);
      } else {
        callback(false);
      }
    } else {
      callback(false);
    }
  });
};

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
