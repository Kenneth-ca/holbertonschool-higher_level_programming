#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
const internal = [];
for (const key in dict) {
  internal.push(key);
  newDict[dict[key]] = internal;
}
console.log(newDict);
