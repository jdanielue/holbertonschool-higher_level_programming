#!/usr/bin/node
let a;
for (let count= 0; count< Math.floor(list.length / 2); i++) {
    a = list[count];
    list[count] = list[list.length - count- 1];
    list[list.length - count- 1] = a;
}
return (list);
};
exports.esrever = function (list) {