#!/usr/bin/node
const a = `${process.argv[2]}`;

function recursion (a) {
  if (isNaN(Number(a)) || a <= 1) {
    return 1;
  } else {
    return a * recursion(a - 1);
  }
}
console.log(recursion(a));
