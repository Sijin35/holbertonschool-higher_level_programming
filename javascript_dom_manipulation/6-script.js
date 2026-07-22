#!/usr/bin/node

async function getName() {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();

  document.querySelector('#character').innerHTML = data.name;
}

getName()
  .catch(error => {console.log(error)});
