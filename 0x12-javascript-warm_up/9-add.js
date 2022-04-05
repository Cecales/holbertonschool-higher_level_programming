#!/usr/bin/node
const value = process.argv;
const a = parseInt(value[2]);
const b = parseInt(value[3]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
