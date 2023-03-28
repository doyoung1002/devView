// swiper.js
const swiper = new Swiper(".mySwiper", {
  autoplayDisableOnInteraction: false,
  loopAdditionalSlides: 1,
  loop: true,
  speed: 2000,
  slidesPerView: 3,
  spaceBetween: 30,
  autoplay: {
    deplay: 0,
    delay: 2000,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});