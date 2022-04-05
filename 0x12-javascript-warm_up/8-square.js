#!/usr/bin/node
const value = process.argv;
const side = parseInt(value[2]);
let x;

if (isNaN(side)) {
  console.log('Missing size');
} else {
  for (x = 0; x < side; x++) {
    console.log('X'.repeat(side));
  }
}
