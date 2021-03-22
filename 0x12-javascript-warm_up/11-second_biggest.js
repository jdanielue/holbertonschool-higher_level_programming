#!/usr/bin/node
let array = process.argv;
array = array.sort();
array.splice(0, 2);
console.log(array);

if (array.length <= 1) {
    console.log(0)
}
else {
    console.log(array[array.length - 2]);
}
