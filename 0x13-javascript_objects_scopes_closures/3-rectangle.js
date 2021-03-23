#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
    print () {
      const forma = 'X';
      for (let contador = 1; contador <= this.height; contador++) {
        console.log(forma.repeat(this.width));
      }
    }
};
