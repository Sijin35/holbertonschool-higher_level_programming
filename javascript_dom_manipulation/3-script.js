const h = document.querySelector('header');
const t = document.querySelector('#toggle_header');

t.addEventListener('click', () => {
  h.classList.toggle('green');
  h.classList.toggle('red');
});
