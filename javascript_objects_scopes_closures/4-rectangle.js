#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    if (
      typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0
    ) { Object.assign(this, { width, height }); }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;

      for (; j < this.width; ++j) {
        process.stdout.write('X');
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
