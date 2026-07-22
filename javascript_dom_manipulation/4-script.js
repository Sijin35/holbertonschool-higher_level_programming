const target = document.querySelector('.my_list');
const a = document.querySelector('#add_item');


a.addEventListener('click', () => {
  const l = document.createElement('li');
  l.textContent = 'Item';
  target.appendChild(l);
});