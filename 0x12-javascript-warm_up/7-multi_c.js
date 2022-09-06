#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  for (let index = 0; index < n.length; index++) {
    // const element = n[index];
    console.log("C is fun");
  }
} else {
  console.log('Missing number of occurrences');
}