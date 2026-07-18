#!/usr/bin/node

const num = parseInt(process.argv[2]);
let fac;

if (Number.isNaN(num)) {
  fac = 1;
}

function factorial (num) {
  if (num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

console.log(factorial(num));
