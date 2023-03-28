const navToggleBtn = document.querySelector('.navbar__toggle');
const navbarMenu = document.querySelector('.navbar__menu');

navToggleBtn.addEventListener('click', () => {
  navbarMenu.classList.toggle('open');
});