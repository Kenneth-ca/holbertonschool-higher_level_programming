#!/usr/bin/node

const SquareBase = require('./5-square');
module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (typeof c === 'undefined') { this.print(); } else {
      let i;
      for (i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
