#!/usr/bin/node

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let bodyDict = 0;
    bodyDict = JSON.parse(body);
    console.log(bodyDict.title);
  }
}
request(options, callback);
