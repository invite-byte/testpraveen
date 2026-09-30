/* ==========================================================
   EVOLTPARTS ENGINEERING PLATFORM INTERACTIVE CONTROLLER
   ========================================================== */

document.addEventListener('DOMContentLoaded', () => {

    /* =====================================================
       NAVBAR SCROLL TRANSITION
       ===================================================== */

    const navbar = document.querySelector('.ev-navbar');

    if (navbar) {

        const handleNavbarScroll = () => {

            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

        };

        // Run once when page loads
        handleNavbarScroll();

        // Run when scrolling
        window.addEventListener(
            'scroll',
            handleNavbarScroll,
            { passive: true }
        );
    }


    /* =====================================================
       PROFILE DROPDOWN
       ===================================================== */

    const profileButton =
        document.getElementById("profileAvatarBtn");

    const profileDropdown =
        document.getElementById("profileDropdown");


    if (profileButton && profileDropdown) {

        profileButton.addEventListener("click", function (event) {

            event.stopPropagation();

            const isOpen =
                profileDropdown.classList.contains("show");


            if (isOpen) {

                profileDropdown.classList.remove("show");

                profileButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

            } else {

                profileDropdown.classList.add("show");

                profileButton.setAttribute(
                    "aria-expanded",
                    "true"
                );

            }

        });


        document.addEventListener("click", function () {

            profileDropdown.classList.remove("show");

            profileButton.setAttribute(
                "aria-expanded",
                "false"
            );

        });


        profileDropdown.addEventListener(
            "click",
            function (event) {

                event.stopPropagation();

            }
        );

    }


    /* =====================================================
       SECTION 02
       INTERACTIVE SYSTEM BREAKDOWN
       ===================================================== */

    const systemItems =
        document.querySelectorAll('.system-item');

    const activeSysImg =
        document.getElementById('active-sys-img');


    if (systemItems.length > 0 && activeSysImg) {

        systemItems.forEach(item => {

            item.addEventListener('mouseenter', () => {

                // Remove active class from all
                systemItems.forEach(i =>
                    i.classList.remove('active')
                );

                // Add active class to hovered item
                item.classList.add('active');


                // Get image
                const newImgSrc =
                    item.getAttribute('data-img');

                const itemIndex =
                    item.getAttribute('data-index');


                // Image fade
                activeSysImg.style.opacity = '0.3';


                setTimeout(() => {

                    activeSysImg.src = newImgSrc;

                    activeSysImg.style.opacity = '1';

                }, 150);


                // Update diagnostic label
                const metaTag =
                    document.querySelector('.preview-meta-tag');


                if (metaTag) {

                    metaTag.textContent =
                        `LIVE DIAGNOSTIC FEED // 0${parseInt(itemIndex) + 1}`;

                }

            });

        });

    }


    /* =====================================================
       SMOOTH SCROLL
       ===================================================== */

    document
        .querySelectorAll('a[href^="#"]')
        .forEach(anchor => {

            anchor.addEventListener('click', function (e) {

                const targetId =
                    this.getAttribute('href');


                if (targetId === '#') {
                    return;
                }


                const targetElement =
                    document.querySelector(targetId);


                if (targetElement) {

                    e.preventDefault();


                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });

                }

            });

        });


    /* =====================================================
       ENGINEERING CONSOLE
       ===================================================== */

    console.log(
        "%c EVOLT PARTS // SYSTEM ARCHITECTURE ACTIVE ",
        "background: #1b4332; color: #d8f3dc; font-family: monospace; padding: 4px 8px; font-weight: bold;"
    );

});