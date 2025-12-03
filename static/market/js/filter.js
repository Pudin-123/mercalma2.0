document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('filter-form');
  if(!form) return;
  const container = document.getElementById('product-container');
  let timeout = null;
  form.addEventListener('input', function(e) {
    if(e.target.name !== 'q') return;
    if(timeout) clearTimeout(timeout);
    timeout = setTimeout(fetchResults, 350);
  });
  function fetchResults(){
    const fd = new FormData(form);
    const params = new URLSearchParams(fd).toString();
    fetch('?' + params, { headers: {'X-Requested-With':'XMLHttpRequest'} })
      .then(r => r.text()).then(html => { container.innerHTML = html; });
  }
});
