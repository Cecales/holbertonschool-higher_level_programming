#!/usr/bin/node
const myVar = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let lang;
for (lang in myVar) {
  console.log(myVar[lang]);
}
