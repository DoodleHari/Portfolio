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

// Function to vertically center sections within the viewport
function centerSectionsVertically() {
    var sections = document.querySelectorAll('.center-vertical');
    var windowHeight = window.innerHeight;

    sections.forEach(function(section) {
        var sectionHeight = section.clientHeight;
        var paddingTop = (windowHeight - sectionHeight) / 2;
        section.style.paddingTop = paddingTop + 'px';
    });
}

// Call the function when the page is loaded and resized
window.addEventListener('load', centerSectionsVertically);
window.addEventListener('resize', centerSectionsVertically);

// this function is used for the preloading
window.addEventListener('load', function() {
    let preloader = document.getElementById('preloader');
    let content = document.getElementById('content');

    setTimeout(function() {
        preloader.style.display = 'none';
        content.style.display = 'block';
    }, 6000); // 5000 milliseconds = 5 minutes
});


function openContactSection() {
    var contactSection = document.getElementById("contact");
    if (contactSection) {
        contactSection.scrollIntoView({ behavior: "smooth" });
    }
}

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})