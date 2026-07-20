#!/usr/bin/node

const num = process.argv.slice(2);

if (num.length <= 1){
  console.log(0);
} else {
  num.sort((a, b) => a - b);
  console.log(num);
}
