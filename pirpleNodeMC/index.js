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

const server = http.createServer((req, res) => {
  // Get the Url and parse it
  const parsedUrl = url.parse(req.url, true);

  // Get the path

  // Send the response
  res.end('Hello Wolrd\n');

  // log the request path
  console.log(parsedUrl);
});

server.listen(3000, () => {
  console.log('The server is listening on port 3000');
});
