#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv[2]) {
  console.log(process.argv.slice(2, 3).join(' '));
}
