#!/usr/bin/node
const value = process.argv;
const toNumber = parseInt(value[2]);
if (isNaN(toNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', toNumber);
}
