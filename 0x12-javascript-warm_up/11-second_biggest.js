#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
    console.log('0');
  } else {
    let i = 2;
    const myArray = [];
    while (process.argv[i]) {
      myArray[i - 2] = process.argv[i];
      i++;
    }
    const secondLargest = myArray.sort(function (a, b) { return a - b; })[myArray.length - 2];
    console.log(secondLargest);
  }