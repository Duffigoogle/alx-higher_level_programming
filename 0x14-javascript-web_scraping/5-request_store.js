#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
// ./5-request_store.js http://loripsum.net/api loripsum

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) { return console.log(err); }
    });
  }
});
