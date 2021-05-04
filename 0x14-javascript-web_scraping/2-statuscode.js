#! /usr/bin/node

const https = require('https');

https.get(process.argv[2], (res) => {
  console.log('statusCode:', res.statusCode);
});