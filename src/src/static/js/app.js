let dash = addEventListener("DOMContentLoaded", () => {
  const btn_menu = document.querySelector(".btn_menu");
  if (btn_menu) {
    btn_menu.addEventListener("click", () => {
      const menu_items = document.querySelector(".menu_items");
      menu_items.classList.toggle("show");
    });
  }
});

$(document).ready(() => {
  $(window).scroll(function () {
    if ($(this).scrollTop() > 0) {
      $("header").addClass("header2");
    } else {
      $("header").removeClass("header2");
    }
  });
});
