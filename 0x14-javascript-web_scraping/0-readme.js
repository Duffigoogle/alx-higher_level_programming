#!/usr/bin/node
// Script that reads and prints the content of a file.
// ./0-readme.js cisfun

const fs = require('fs');

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, result) {
  if (err) {
    return console.log(err);
  }
  console.log(result);
});
