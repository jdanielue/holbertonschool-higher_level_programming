#!/usr/bin/node
let array = process.argv;
array = array.sort();
array.splice(0, 3);
console.log(array[array.length - 2]);
