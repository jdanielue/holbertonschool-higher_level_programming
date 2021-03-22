#!/usr/bin/node

for (let largo = 1; largo <= `${process.argv[2]}`; largo++) {
    for (let ancho = 1; ancho <= `${process.argv[2]}`; ancho++) {
        process.stdout.write('X');
    }
    process.stdout.write('\n');
}
