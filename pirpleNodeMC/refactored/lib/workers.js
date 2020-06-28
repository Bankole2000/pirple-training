/*
 * Worder related tasks
 */

// Dependencies
const path = require('path');
const fs = require('fs');
const _data = require('./data');
const https = require('https');
const http = require('http');
const helpers = require('./helpers');
const url = require('url');
const _logs = require('./logs');

// OBJECT: Instantiate the worker object
const workers = {};

// FUNC: to gather all the checks
workers.gatherAllChecks = () => {
  // Get all the checks that exist in the system
  _data.list('checks', (err, checks) => {
    if (!err && checks && checks.length > 0) {
      checks.forEach((check) => {
        // Read in the check data
        _data.read('checks', check, (err, originalCheckData) => {
          if (!err && originalCheckData) {
            // Pass the data to the check validator, and let that function continue or log errors as needed
            workers.validateCheckData(originalCheckData);
          } else {
            console.log("Error reading one of the check's Data");
          }
        });
      });
    } else {
      console.log('Error: Could not find any checks to process');
    }
  });
};
// FUNC: Sanity Check the check data
workers.validateCheckData = (originalCheckData) => {
  originalCheckData =
    typeof originalCheckData == 'object' && originalCheckData !== null
      ? originalCheckData
      : {};
  originalCheckData.checkId =
    typeof originalCheckData.checkId == 'string' &&
    originalCheckData.checkId.trim().length == 20
      ? originalCheckData.checkId.trim()
      : false;
  originalCheckData.userPhone =
    typeof originalCheckData.userPhone == 'string' &&
    originalCheckData.userPhone.trim().length == 11
      ? originalCheckData.userPhone.trim()
      : false;
  originalCheckData.url =
    typeof originalCheckData.url == 'string' &&
    originalCheckData.url.trim().length > 0
      ? originalCheckData.url.trim()
      : false;
  originalCheckData.protocol =
    typeof originalCheckData.protocol == 'string' &&
    ['http', 'https'].indexOf(originalCheckData.protocol) > -1
      ? originalCheckData.protocol
      : false;
  originalCheckData.method =
    typeof originalCheckData.method == 'string' &&
    ['get', 'post', 'put', 'delete'].indexOf(originalCheckData.method) > -1
      ? originalCheckData.method
      : false;
  originalCheckData.successCodes =
    typeof originalCheckData.successCodes == 'object' &&
    originalCheckData.successCodes instanceof Array &&
    originalCheckData.successCodes.length > 0
      ? originalCheckData.successCodes
      : false;
  originalCheckData.timeoutSeconds =
    typeof originalCheckData.timeoutSeconds == 'number' &&
    originalCheckData.timeoutSeconds % 1 === 0 &&
    originalCheckData.timeoutSeconds >= 1 &&
    originalCheckData.timeoutSeconds <= 5
      ? originalCheckData.timeoutSeconds
      : false;

  // Set the keys that may not be set if the workers have never seen this check before
  originalCheckData.state =
    typeof originalCheckData.state == 'string' &&
    ['up', 'down'].indexOf(originalCheckData.state) > -1
      ? originalCheckData.state
      : 'down';
  originalCheckData.lastChecked =
    typeof originalCheckData.lastChecked == 'number' &&
    originalCheckData.lastChecked > 0
      ? originalCheckData.lastChecked
      : false;

  // If all the checks pass pass the data along to the next step in the process
  if (
    originalCheckData.checkId &&
    originalCheckData.userPhone &&
    originalCheckData.url &&
    originalCheckData.method &&
    originalCheckData.protocol &&
    originalCheckData.successCodes &&
    originalCheckData.timeoutSeconds
  ) {
    workers.performCheck(originalCheckData);
  } else {
    console.log(
      'Error: one of the checks is not properly formatted. Skipping it: ',
      originalCheckData
    );
  }
};

workers.performCheck = (originalCheckData) => {
  // prepare the initial check outcome
  const checkOutcome = {
    error: false,
    response: false,
  };

  // Mark that the outcome has not been sent yet
  let outcomeSent = false;

  // Parse the host name and the path out of the original Check Data
  const parsedUrl = url.parse(
    `${originalCheckData.protocol}://${originalCheckData.url}`
  );
  const hostname = parsedUrl.hostname;
  const path = parsedUrl.path; // note that we are using path and not pathname because we want the full query string

  // Construct the request
  const requestDetails = {
    protocol: `${originalCheckData.protocol}:`,
    hostname,
    method: originalCheckData.method,
    path,
    timeout: originalCheckData.timeoutSeconds * 1000,
  };

  // perform the http request - instantiate the request using either http or https module
  const _moduleToUse = originalCheckData.protocol == 'http' ? http : https;
  const req = _moduleToUse.request(requestDetails, (res) => {
    // Grab the status of the sent request
    const status = res.statusCode;

    // update the checkOutcome and pass the data along
    checkOutcome.responseCode = status;
    if (!outcomeSent) {
      workers.processCheckOutcome(originalCheckData, checkOutcome);
      outcomeSent = true;
    }
  });

  // Bind to the error event so it doesn't get thrown
  req.on('error', (e) => {
    // update the checkOutcome and pass the data along
    checkOutcome.error = {
      error: true,
      value: e,
    };
    if (outcomeSent) {
      workers.processCheckOutcome(originalCheckData, checkOutcome);
      outcomeSent = true;
    }
  });

  // Bind to the timeout event
  req.on('timeout', (e) => {
    // update the checkOutcome and pass the data along
    checkOutcome.error = {
      error: true,
      value: 'timeout',
    };
    if (outcomeSent) {
      workers.processCheckOutcome(originalCheckData, checkOutcome);
      outcomeSent = true;
    }
  });
  // End the request
  req.end();
};
// FUNC: process the check outcome, and update the check data as needed and trigger an alert to the user if needed
// FUNC: special logic for checks that have never been test before
workers.processCheckOutcome = (originalCheckData, checkOutcome) => {
  // Decide if the check is considered up or down
  const state =
    !checkOutcome.error &&
    checkOutcome.responseCode &&
    originalCheckData.successCodes.indexOf(checkOutcome.responseCode) > -1
      ? 'up'
      : 'down';

  // Decide if an alert is warranted
  const alertWarranted =
    originalCheckData.lastChecked && originalCheckData.state !== state
      ? true
      : false;

  // ADMIN: log to the console
  const timeOfCheck = Date.now();
  workers.log(
    originalCheckData,
    checkOutcome,
    state,
    alertWarranted,
    timeOfCheck
  );

  // Update the check data
  const newCheckData = originalCheckData;
  newCheckData.state = state;
  newCheckData.lastChecked = timeOfCheck;

  // STORE: Save the updates
  _data.update('checks', newCheckData.checkId, newCheckData, (err) => {
    if (!err) {
      // Send the new check data to the next phase in the process if needed
      if (alertWarranted) {
        workers.alertUserToStatusChange(newCheckData);
      } else {
        console.log('Check outcome has not changed, no alert needed');
      }
    } else {
      console.log(
        'Error trying to save new check data to check with id: ',
        newCheckData.checkId
      );
    }
  });
};

// FUNC: send alert to user to change in one of their check status if needed
workers.alertUserToStatusChange = (newCheckData) => {
  const msg = `Alert: Your check for ${newCheckData.method.toUpperCase()} ${
    newCheckData.protocol
  }://${newCheckData.url} is currently ${newCheckData.state}`;
  helpers.sendTwilioSms(newCheckData.userPhone, msg, (err) => {
    if (!err) {
      console.log(
        'Success: User was alerted to a status change in their check via sms. Message was: ',
        msg
      );
    } else {
      console.log(
        'Error: Could not send SMS to user who had a state change in one of their checks: ',
        newCheckData
      );
    }
  });
};

workers.log = (
  originalCheckData,
  checkOutcome,
  state,
  alertWarranted,
  timeOfCheck
) => {
  // Form the log data
  const logData = {
    check: originalCheckData,
    outcome: checkOutcome,
    state,
    alert: alertWarranted,
    time: timeOfCheck,
  };

  // Convert data to a string
  const logString = JSON.stringify(logData);

  // Determing the name of the log file
  const logFileName = originalCheckData.checkId;

  // Append the log string ot the file
  _logs.append(logFileName, logString, (err) => {
    if (!err) {
      console.log('Logging to file succeeded');
    } else {
      console.log('Loggine to the file failed');
    }
  });
};

// FUNC: Timer to execute the workers process once per minute
workers.loop = () => {
  setInterval(() => {
    workers.gatherAllChecks();
  }, 1000 * 60);
};

// Function to rotate (aka compress) log files
workers.rotateLogs = () => {
  // List all the non compressed log files
  _logs.list(false, (err, logs) => {
    if (!err && logs && logs.length > 0) {
      logs.forEach((logName) => {
        let logId = logName.replace('.log', '');
        let newFileId = `${logId}-${Date.now()}`;
        _logs.compress(logId, newFileId, (err) => {
          if (!err) {
            // Truncate the log
            _logs.truncate(logId, (err) => {
              if (!err) {
                console.log('Success truncating logFile');
              } else {
                console.log('Error truncating logFile', err);
              }
            });
          } else {
            console.log('Error compressing one of the logs files', err);
          }
        });
      });
    } else {
      console.log('Error, could not find any logs to rotate');
    }
  });
};

// Timer to execute the log-rotation process once per day
workers.logRotationLoop = () => {
  setInterval(() => {
    workers.rotateLogs();
  }, 1000 * 60 * 60 * 24);
};

// FUNC: Init script for worders
workers.init = () => {
  // Send to console in yellow
  console.log('\x1b[33m%s\x1b[0m', 'Background workers started');

  // Execute all the checks immediate
  workers.gatherAllChecks();
  // Call a loop so the checks continue to execute on their own
  workers.loop();

  // Compress all logs immediately
  workers.rotateLogs();

  // Call the compression loops so logs will be compressed later on
  workers.logRotationLoop();
};

// Export the worker module
module.exports = workers;
