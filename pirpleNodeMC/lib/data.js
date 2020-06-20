/*  FILE: data.js FOLDER: lib
 * File: lib/data.js
 * Auth: Bankole Esan
 * Desc: Library for writing all the data to the fs
 * Task: RESTful JSON API
 */

//  NOTE: Designed with ERROR BACK pattern. i.e.
// NOTE: basically callback errors till function achieves desired end

//  SECTION: Dependencies
const fs = require('fs');
const path = require('path');
// endOfSection:

// CONTAINER: Container for the module (to be exported)
const lib = {};

// Define base directory of the data folder
lib.baseDir = path.join(__dirname, '/../.data/');

// FUNCTION: CREATE: Write data to a new file
lib.create = (dir, file, data, callback) => {
  // subFunction: Open/Create the file for writing
  fs.open(`${lib.baseDir}${dir}/${file}.json`, 'wx', (err, fileDescriptor) => {
    if (!err && fileDescriptor) {
      // Convert data to string
      const stringData = JSON.stringify(data);

      // subFunction: Write to file and close it
      fs.writeFile(fileDescriptor, stringData, (err) => {
        if (!err) {
          fs.close(fileDescriptor, (err) => {
            if (!err) {
              callback(false);
            } else {
              callback('Error closing new file');
            }
          });
        } else {
          callback('Error writing to new file');
        }
      });
    } else {
      callback('Could not create new file, it may already exist');
    }
  });
};

// FUNCTION: READ: Read data from a file
lib.read = (dir, file, callback) => {
  fs.readFile(`${lib.baseDir}${dir}/${file}.json`, 'utf8', (err, data) => {
    callback(err, data);
  });
};

// FUNCTION: UPDATE: Update data in a file
lib.update = (dir, file, data, callback) => {
  // subFunction: Open/Create the file for writing
  fs.open(`${lib.baseDir}${dir}/${file}.json`, 'r+', (err, fileDescriptor) => {
    if (!err && fileDescriptor) {
      // Convert data to string
      const stringData = JSON.stringify(data);

      // subFunction: truncate the file
      fs.ftruncate(fileDescriptor, (err) => {
        if (!err) {
          // subFunction: Write to file and close it
          fs.writeFile(fileDescriptor, stringData, (err) => {
            if (!err) {
              fs.close(fileDescriptor, (err) => {
                if (!err) {
                  callback(false);
                } else {
                  callback('Error closing new file');
                }
              });
            } else {
              callback('Error writing to existing file');
            }
          });
        } else {
          callback('Error truncating the file');
        }
      });
    } else {
      callback('Could not open the file for update, it may not exist yet');
    }
  });
};

// FUNCTION: DELETE:
lib.delete = (dir, file, callback) => {
  // subFunction: Unlink the file - i.e. Delete
  fs.unlink(`${lib.baseDir}${dir}/${file}.json`, (err) => {
    if (!err) {
      callback(false);
    } else {
      callback('Error deleting the file');
    }
  });
};

// Export the module
module.exports = lib;
