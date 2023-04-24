#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    if (
      typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0
    ) { Object.assign(this, { width, height }); }
  }

  print () {
    console.log('X'.repeat(this.width).concat('\n').repeat(this.height));
  }
};
