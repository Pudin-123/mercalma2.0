
// Theme toggle: reads/writes data-theme on documentElement and saves preference to localStorage
(function(){
  const toggle = document.getElementById('theme-toggle-btn');
  const icon = document.getElementById('theme-toggle-icon');
  const current = localStorage.getItem('theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark':'light');
  if(current === 'dark') document.documentElement.setAttribute('data-theme','dark');

  function updateIcon(){
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if(icon) icon.textContent = isDark ? '🌙' : '☀️';
  }
  updateIcon();

  if(toggle){
    toggle.addEventListener('click', ()=>{
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if(isDark){
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme','light');
      } else {
        document.documentElement.setAttribute('data-theme','dark');
        localStorage.setItem('theme','dark');
      }
      updateIcon();
    });
  }
})();
