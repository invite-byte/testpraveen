document.addEventListener("DOMContentLoaded", function () {


const profileButton = document.getElementById("profileAvatarBtn");
const profileDropdown = document.getElementById("profileDropdown");

if (!profileButton || !profileDropdown) {
    console.error("Profile button or profile dropdown not found.");
    return;
}

/* Open / close profile popup */
profileButton.addEventListener("click", function (event) {

    event.stopPropagation();

    const isOpen = profileDropdown.classList.contains("show");

    if (isOpen) {
        profileDropdown.classList.remove("show");
        profileButton.setAttribute("aria-expanded", "false");
    } else {
        profileDropdown.classList.add("show");
        profileButton.setAttribute("aria-expanded", "true");
    }
});


/* Prevent popup click from closing itself */
profileDropdown.addEventListener("click", function (event) {
    event.stopPropagation();
});


/* Click anywhere outside → close popup */
document.addEventListener("click", function () {

    profileDropdown.classList.remove("show");
    profileButton.setAttribute("aria-expanded", "false");

});


/* Press ESC → close popup */
document.addEventListener("keydown", function (event) {

    if (event.key === "Escape") {

        profileDropdown.classList.remove("show");
        profileButton.setAttribute("aria-expanded", "false");

    }

});


});
