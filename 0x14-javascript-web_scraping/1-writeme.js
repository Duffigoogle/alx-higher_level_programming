#!/usr/bin/node
// Script that writes a string to a file.
// ./1-writeme.js my_file.txt "Python is cool"

const fs = require('fs');

const filename = process.argv[2];
const text = process.argv[3];

fs.writeFile(filename, text, 'utf-8', (err) => {
  if (err) {
    return console.log(err);
  }
});
