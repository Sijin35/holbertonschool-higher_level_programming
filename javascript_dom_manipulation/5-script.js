const u = document.querySelector('#update_header');
const h = document.querySelector('header');

u.addEventListener('click', () => {
  h.textContent = 'New Header!!!'
});