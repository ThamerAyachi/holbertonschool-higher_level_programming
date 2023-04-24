#!/usr/bin/node

exports.converter = (base) => {
  const myConverter = (n) => n.toString(base);
  return myConverter;
};
