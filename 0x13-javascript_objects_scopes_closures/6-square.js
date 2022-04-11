#!/usr/bin/node

const SquareBase = require('./-square');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    super.print(c);
  }
};
