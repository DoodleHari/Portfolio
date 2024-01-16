function openNav() {
    document.getElementById("sidenav").style.width = "100%";
}

function closeNav() {
    document.getElementById("sidenav").style.width = "0";
}

document.addEventListener('DOMContentLoaded', function () {
    // Toggle the visibility of the side navigation when the menu button is clicked
    document.querySelector('.menu-btn').addEventListener('click', function () {
        openNav();
    });
});

function toolbar() {
    document.getElementById("about").style.margin = "";
}



