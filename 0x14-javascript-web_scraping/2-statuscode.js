#!/usr/bin/node
// Script that display the status code of a GET request.
// ./2-statuscode.js https://intranet.hbtn.io/status

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return (console.log(error));
  }
  console.log('code: ' + response.statusCode);
});
