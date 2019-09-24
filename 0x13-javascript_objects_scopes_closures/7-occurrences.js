#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter(function counting (val, index, arr) {
    return val === searchElement;
  });
  const count = newList.length;
  return count;
};
