#!/usr/bin/node

module.exports = class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      const forma = 'X';
      for (let contador = 1; contador <= this.width; contador++) {
        console.log(forma.repeat(this.height));
      }
    };
  }
};
