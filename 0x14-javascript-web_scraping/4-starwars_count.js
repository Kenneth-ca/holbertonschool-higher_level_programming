#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let i; let j; let count = 0;
    const results = JSON.parse(body).results;
    for (i = 0; i < results.length; i++) {
      for (j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
