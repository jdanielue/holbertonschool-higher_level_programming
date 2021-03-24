#!/usr/bin/node
let ocr = 0;
exports.logMe = function (item) {
  console.log(`${ocr}:`, item);
  ocr++
};