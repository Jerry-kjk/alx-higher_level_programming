#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((a, i) => a * i);
console.log(list);
console.log(newList);
