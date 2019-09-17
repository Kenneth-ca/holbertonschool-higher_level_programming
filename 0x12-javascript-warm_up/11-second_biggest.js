#!/usr/bin/node
function sorting (a, b) {
  return a - b;
}
if (process.argv.length < 3) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2);
  array.sort(sorting);
  array.pop();
  console.log(array.pop());
}
