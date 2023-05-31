document.addEventListener("DOMContentLoaded", () => {
  if(is_touch_enabled() === true) {
    // touchscreen
    
    document.querySelectorAll('.card__share').forEach((element) => {
      element.classList.remove("card__hovered");
    });
  }

  let formContainer = document.getElementById("form-container");

  bindFormClick();

  function bindFormClick() {
    document
      .getElementById("form-container")
      .addEventListener("click", function _listner(e) {
        console.log("test");
        e.preventDefault();
        toggleForm();

        document
          .getElementById("form-container")
          .removeEventListener("click", _listner);
      });
  }

  $("#form-close, .form-overlay").click(function (e) {
    e.stopPropagation();
    e.preventDefault();
    toggleForm();
    bindFormClick();
  });

  function toggleForm() {
    document.getElementById("form-container").classList.toggle("expand");
    // document.getElementById("form-container").children().classList.toggle("expand");
    children = document.querySelector("#form-container").children;

    document.querySelector('#form-container').classList.toggle("dNoneB");


    for (var i = 0; i < children.length; i++) {
      children[i].classList.toggle("expand");
    }
    document.querySelector("body").classList.toggle("show-form-overlay");
  }

  document.getElementById("start_date").onchange = function () {
    let start = document.getElementById("start_date").value;
    document.getElementById("end_date").min = start;
    if (document.getElementById("end_date").value <= start) {
      document.getElementById("end_date").value = start;
    }
  };

  document.getElementById("end_date").onchange = function () {
    if (document.getElementById("start_date").value > document.getElementById("end_date")) {
      document.getElementById("start_date").value = document.getElementById("end_date");
    }
  };
});
