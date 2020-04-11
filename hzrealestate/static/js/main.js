const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

// Used to create a fade out effect
setTimeout(function () {
  $("#message").fadeOut("slow");
}, 3000);
