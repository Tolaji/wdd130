function toggleMenu() {
  var menuContent = document.getElementById("menu-content");

  if (menuContent.style.display === "none") {
    menuContent.style.display = "block";
    document.getElementById("menu-icon").src = "img/close.png";
    window.location.href = "navigation.html";
  } else {
    menuContent.style.display = "none";
    document.getElementById("menu-icon").src = "img/menu.png";
  }
}
