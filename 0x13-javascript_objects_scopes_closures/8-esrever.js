#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  for (let index = list.length - 1; index >= 0; index--) {
    arr.push(list[index]);
  }
  return (arr);
};
