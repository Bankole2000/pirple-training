/*
 * File: index.js
 * Auth: Bankole Esan
 * Desc: Pirple.com NodeJS Homework #1
 * Task: RESTful JSON API
 */

// Dependecies
const http = require('http');
const url = require('url');
const StringDecoder = require('string_decoder').StringDecoder;
// ☝️ used to parse payload (body of the )

const server = http.createServer((req, res) => {
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
      payload: buffer,
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
      console.log(parsedUrl);
    });
  });
});

server.listen(3000, () => {
  console.log('The server is listening on port 3000');
});

const handlers = {};

handlers.notFound = (data, callback) => {
  callback(404, {
    error: true,
    message: "This Route doesn't exist! i.e. Not Found",
  });
};

handlers.sample = (data, callback) => {
  callback(406, { error: false, name: 'sample Handler' });
};

handlers.hello = (data, callback) => {
  callback(200, {
    error: false,
    message: 'Welcome to the Node JS Master Class',
  });
};

const router = {
  sample: handlers.sample,
  notFound: handlers.notFound,
  hello: handlers.hello,
};
