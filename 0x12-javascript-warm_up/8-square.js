#!/usr/bin/node
let array = [];
const letra = 'X';

for (let largo = 1; largo <= `${process.argv[2]}`; largo++) {
  array = [];
  for (let ancho = 1; ancho <= `${process.argv[2]}`; ancho++) {
    array.push(letra);
  }
  console.log(array.join(''));
}
