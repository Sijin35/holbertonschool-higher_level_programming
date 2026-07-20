#!/usr/bin/node

const num = process.argv.slice(2);

if (num.length <= 2) {
  console.log(0);
} else {
  num.sort((a, b) => b - a);
  console.log(num[1]);
}
