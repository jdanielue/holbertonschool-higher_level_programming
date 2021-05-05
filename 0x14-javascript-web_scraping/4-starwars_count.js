#!/usr/bin/node

const request = require('request');

request(process.argv[2], function callback (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const dictBody = JSON.parse(body).results;
  let count = 0;
  for (const element of dictBody) {
    for (const movie of element.characters) {
      if (movie === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
