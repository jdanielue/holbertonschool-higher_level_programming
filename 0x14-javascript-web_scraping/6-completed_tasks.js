#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonbody = JSON.parse(body);
  const newdict = {};
  let contador = 0;
  let usridCounter = 0;
  for (const element of jsonbody) {
    if (usridCounter !== element.userId) {
      contador = 0;
      usridCounter = element.userId;
    }
    if (element.completed === true) {
      contador += 1;
      newdict[element.userId] = contador;
    }
  }
  console.log(newdict);
});
