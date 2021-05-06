#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonbody = JSON.parse(body);
  const newdict = {};
  let contador;
  let usridCounter;
  for (const element of jsonbody) {
    usridCounter = element.userId;
    contador = element.completed;
    if (contador) {
      if (!newdict[usridCounter]) {
        newdict[usridCounter] = 0;
      }
      newdict[usridCounter] += 1;
    }
  }
  console.log(newdict);
});
