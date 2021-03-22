#!/usr/bin/node
let array = process.argv;
array = array.sort();
array.splice(0, 2);

if (array.length <= 1) {
  console.log(0);
} else if (array[array.length - 2] === array[array.length - 1])
    console.log(undefined);
else {
  console.log(array[array.length - 2]);
}
