#!/usr/bin/node

const h = document.querySelector('header');
const r = document.querySelector('#red_header');

r.addEventListener('click', () => {
    h.classList.add('red');
    // h.classList.toggle('red');
});
