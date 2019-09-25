#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const newDict = {};
    for (const key of JSON.parse(body)) {
      if (key.completed) {
        if (newDict[key.userId]) {
          newDict[key.userId] += 1;
        } else {
          newDict[key.userId] = 1;
        }
      }
    }
    console.log(newDict);
  }
});
