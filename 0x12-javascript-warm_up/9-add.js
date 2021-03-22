#!/usr/bin/node

function add (a, b) {
  if (isNaN(Number(a) || isNaN(Number(b)))) {
    console.log(NaN);
  }
  console.log(Number(a) + Number(b));
}
const a = `${process.argv[2]}`;
const b = `${process.argv[3]}`;
add(a, b);
