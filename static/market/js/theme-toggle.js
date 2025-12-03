document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('theme-toggle');
  if(!toggle) return;
  const body = document.body;
  const saved = localStorage.getItem('theme');
  if(saved) body.setAttribute('data-theme', saved);
  toggle.addEventListener('click', () => {
    const cur = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', cur);
    localStorage.setItem('theme', cur);
  });
});
