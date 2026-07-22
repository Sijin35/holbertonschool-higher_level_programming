#!/usr/bin/node

async function getTitle() {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const data = await response.json();

  const newList = document.querySelector('#list_movies');
  data.results.forEach(name => {
    const l = document.createElement('li');
    l.textContent = name.title;
    newList.appendChild(l);
  });
};

getTitle()
  .catch(error => {console.log('error')});