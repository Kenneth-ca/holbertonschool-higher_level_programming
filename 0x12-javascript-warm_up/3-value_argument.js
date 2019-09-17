#!/usr/bin/node
let count = 0;
process.argv.forEach((val, index, array) => {
  count++;
});
if (count <= 2) {
  console.log('No argument');
}
if (count > 2) {
  console.log(process.argv[2]);
}
