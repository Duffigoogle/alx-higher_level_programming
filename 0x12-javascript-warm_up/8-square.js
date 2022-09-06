#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
let i = num;
if (!isNaN(num) && num > 0) {
  for (i; i !== 0; i--) {
    console.log('X'.repeat(num));
  }
} else if (isNaN(num)) {
  console.log('Missing size');
}