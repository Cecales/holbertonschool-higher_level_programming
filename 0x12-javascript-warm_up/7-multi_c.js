#!/usr/bin/node
const value = process.argv;
const x = parseInt(value[2]);
let loop = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (loop < x) {
    console.log('C is fun');
    loop++;
  }
}
