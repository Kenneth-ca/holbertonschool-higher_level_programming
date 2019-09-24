#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i;
  for (i = list.length; i > 0; i--) {
    newList.push(list[i - 1]);
  }
  return newList;
};
