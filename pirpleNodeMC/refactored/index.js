/*
 * Main index file that calls server
 * and background workers
 *
 *
 */

// Dependencies
const server = require('./lib/server');
const workers = require('./lib/workers');

// Declare the app
const app = {};

// FUNCTION: Init
app.init = () => {
  // subFunction: start the server
  server.init();

  // subFunction: Start the workers
  // workers.init();
};

// Execute
app.init();

// Export the app
module.exports = app;
