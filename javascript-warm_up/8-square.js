#!/usr/bin/node

const c = parseInt(process.argv[2]);

if (Number.isNaN(c)) {
  console.log('Missing size');
}

for (let i = 0; i < c; i++) {
  let row = '';
  for (let j = 0; j < c; j++) {
    row += 'X';
  }
  console.log(row);
}
