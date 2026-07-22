#!/usr/bin/node

async function getHello() {
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  const data = await response.json();

  console.log(data);
  document.querySelector('#hello').innerHTML = data.hello;
}

getHello()
  .catch(error => {console.log('error')});