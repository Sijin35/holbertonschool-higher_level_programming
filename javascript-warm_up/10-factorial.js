#!/usr/bin/node

const num = parseInt(process.argv[2]);
let fac = 1;

for (let i = 1; i <= num; i++) {
  fac *= i;
}

if (Number.isNaN(num)) {
  fac = 1;
}

console.log(fac);
