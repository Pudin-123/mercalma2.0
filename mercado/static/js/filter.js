document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("filter-form");

  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      const params = new URLSearchParams(formData).toString();
      window.location = `?${params}`;
    });
  }
});
