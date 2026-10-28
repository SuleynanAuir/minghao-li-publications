const search = document.querySelector('#search');
const entries = [...document.querySelectorAll('#documents li')];
search.addEventListener('input', () => {
  const query = search.value.trim().toLocaleLowerCase();
  let visible = 0;
  entries.forEach(entry => {
    entry.hidden = !entry.querySelector('h2').textContent.toLocaleLowerCase().includes(query);
    if (!entry.hidden) visible++;
  });
  document.querySelector('#count').textContent = `${visible} 份`;
  document.querySelector('#empty').hidden = visible !== 0;
  document.querySelector('#status').textContent = `找到 ${visible} 份文档`;
});
