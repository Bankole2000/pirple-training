/*
 * File: index.js
 * Auth: Bankole Esan
 * Desc: Pirple.com NodeJS Homework #1
 * Task: RESTful JSON API
 */

// SECTION: Dependecies
const http = require('http');
// ☝️ module for handling requests and sending responses
const https = require('https');
// ☝️ module for handling requests but with https
const url = require('url');
// ☝️ used for parsing the url
const fs = require('fs');
// ☝️ used to read files - data and ssl files
const StringDecoder = require('string_decoder').StringDecoder;
// ☝️ used to parse payload (body of the )
const config = require('./lib/config');
// ☝️ used to import exports from config file
const _data = require('./lib/data');
// ☝️ used for writing to the data files
const handlers = require('./lib/handlers');
const helpers = require('./lib/helpers');

// endOfSection:

// TEST: PASSING: CREATE: Syntax for writing to a new file
// _data.create('test', 'newFile', { foo: 'bar' }, (err) => {
//   console.log('This was the error', err);
// });

// TEST: PASSING: READ: Syntax for reading from a file
// _data.read('test', 'newFile', (err, data) => {
//   console.log('This was the error', err, '\nAnd this was the data ', data);
// });

// TEST: PASSING: UPDATE: Syntax for writing to a new file
// _data.update('test', 'newFile', { hodge: 'pudge' }, (err) => {
//   console.log('This was the error', err);
// });

// TEST: PASSING: DELETE: Syntax for writing to a new file
// _data.delete('test', 'newFile', (err) => {
//   console.log('This was the error', err);
// });

// SECTION: HTTP and HTTPS SERVERS
// FEATURE: Http Server
const httpServer = http.createServer((req, res) => {
  unifiedServer(req, res);
});
// Start the server
httpServer.listen(config.httpPort, () => {
  console.log(
    `The server is listening on port ${config.httpPort} in ${config.envName} mode`
  );
}); // endFEAT:
// FEATURE: HTTPS Server
const httpsServerOptions = {
  key: fs.readFileSync('./https/key.pem'),
  cert: fs.readFileSync('./https/cert.pem'),
};
const httpsServer = https.createServer(httpsServerOptions, (req, res) => {
  unifiedServer(req, res);
});
// Start the https server
httpsServer.listen(config.httpsPort, () => {
  console.log(
    `The server is listening on port ${config.httpsPort} in ${config.envName} mode`
  );
}); // endFEAT:
// FEATURE: Unified Server
const unifiedServer = (req, res) => {
  // Get the Url and parse it
  const parsedUrl = url.parse(req.url, true);

  // Get the path FUNCTION: get the path and remove starting and ending slashes
  const path = parsedUrl.pathname; // Untrimmed path
  const trimmedPath = path.replace(/^\/+|\/+$/g, '');

  // Get the Query string as an object
  const queryStringObject = parsedUrl.query;

  // Get the headers as an object
  const headers = req.headers;

  //  Get the HTTP method
  const method = req.method.toUpperCase();

  // FUNCTION: get the buffer
  const decoder = new StringDecoder('utf-8');
  let buffer = '';
  req.on('data', (data) => {
    buffer += decoder.write(data);
  });

  req.on('end', () => {
    buffer += decoder.end();

    // Choose request handler from router object
    const chosenHandler =
      typeof router[trimmedPath] !== 'undefined'
        ? router[trimmedPath]
        : router.notFound;

    // Construct data to send to router object
    const data = {
      trimmedPath,
      queryStringObject,
      headers,
      method,
      payload: helpers.parseJsonToObject(buffer),
    };

    // Route the request to the chosen handler
    chosenHandler(data, (statusCode, payload) => {
      // Use the status code returned from the handler function or set the default to 200
      statusCode = typeof statusCode == 'number' ? statusCode : 200;

      // Use the payload returned from the handler function or set the default to an empty object
      payload = typeof payload == 'object' ? payload : {};

      // Convert the payload to a string
      const payloadString = JSON.stringify(payload);

      // Send the response
      res.setHeader('Content-Type', 'application/json');
      res.writeHead(statusCode);
      res.end(payloadString);

      // log the request path
      console.log(payload);
    });
  });
}; // endFEAT:
//endOfSection:

// SECTION: DESCRIPTION: Handles all routes
const router = {
  sample: handlers.sample,
  notFound: handlers.notFound,
  hello: handlers.hello,
  ping: handlers.ping,
  users: handlers.users,
  tokens: handlers.tokens,
  checks: handlers.checks,
};
// endOfSection:
