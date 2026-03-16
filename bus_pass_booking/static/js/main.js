// Wait until DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {

  /* ===============================
      MOBILE MENU TOGGLE
  =============================== */

  /* ===============================
      SCROLL REVEAL (Safe Version)
  =============================== */

  if (typeof ScrollReveal !== "undefined") {
    const sr = ScrollReveal({
      distance: "50px",
      duration: 1000,
      easing: "ease-in-out",
      origin: "bottom",
      reset: false
    });

    sr.reveal(".header__content h1", { delay: 200 });
    sr.reveal(".header__content p", { delay: 400 });
    sr.reveal(".header__btn", { delay: 600 });
    sr.reveal(".section__header", { delay: 200 });
    sr.reveal(".about__content", { delay: 300 });
    sr.reveal(".service__card", { interval: 200 });
    sr.reveal(".header__image", {
  delay: 300,
  origin: "right",
  distance: "100px",
  duration: 900
});
  }

});