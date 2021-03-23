#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let iter = 1; iter <= x; iter++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;
