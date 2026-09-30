document.addEventListener('DOMContentLoaded', function () {

    // ==========================================
    // GET ELEMENTS
    // ==========================================

    const loginForm = document.getElementById('evLoginForm');

    const emailInput = document.getElementById('id_email');

    const passwordInput = document.getElementById('id_password');

    const togglePasswordBtn =
        document.getElementById('togglePassword');

    const togglePasswordIcon =
        document.getElementById('togglePasswordIcon');

    const submitBtn =
        document.getElementById('loginSubmitBtn');

    const btnText =
        submitBtn.querySelector('.btn-text');

    const btnSpinner =
        submitBtn.querySelector('.btn-spinner');

    const formErrorAlert =
        document.getElementById('formErrorAlert');


    // ==========================================
    // PASSWORD VISIBILITY
    // ==========================================

    togglePasswordBtn.addEventListener('click', function () {

        const type =
            passwordInput.getAttribute('type') === 'password'
                ? 'text'
                : 'password';


        passwordInput.setAttribute('type', type);


        if (type === 'text') {

            togglePasswordIcon.classList.remove('fa-eye');

            togglePasswordIcon.classList.add('fa-eye-slash');

        } else {

            togglePasswordIcon.classList.remove('fa-eye-slash');

            togglePasswordIcon.classList.add('fa-eye');

        }

    });


    // ==========================================
    // EMAIL VALIDATION
    // ==========================================

    function isValidEmail(email) {

        const emailRegex =
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        return emailRegex.test(email);

    }


    // ==========================================
    // EMAIL INPUT
    // ==========================================

    emailInput.addEventListener('input', function () {

        emailInput
            .closest('.ev-input-group')
            .classList.remove('is-invalid');


        const emailError =
            document.getElementById('emailError');


        // emailError.style.display = 'none';


        // Hide Django error only if it exists

        if (formErrorAlert) {

            // formErrorAlert.classList.add('d-none');

        }

    });


    // ==========================================
    // EMAIL BLUR
    // ==========================================

    emailInput.addEventListener('blur', function () {

        const emailError =
            document.getElementById('emailError');


        if (emailInput.value.trim() === '') {

            emailError.textContent =
                'Enter an email first';

            emailError.style.display =
                'block';


            emailInput
                .closest('.ev-input-group')
                .classList.add('is-invalid');

        }


        else if (
            !isValidEmail(emailInput.value.trim())
        ) {

            emailError.textContent =
                'Enter a valid email address';

            emailError.style.display =
                'block';


            emailInput
                .closest('.ev-input-group')
                .classList.add('is-invalid');

        }


        else {

            emailError.textContent = '';

            emailError.style.display =
                'none';


            emailInput
                .closest('.ev-input-group')
                .classList.remove('is-invalid');

        }

    });


    // ==========================================
    // PASSWORD BLUR
    // ==========================================

    passwordInput.addEventListener('blur', function () {

        const passwordError =
            document.getElementById('passwordError');


        if (passwordInput.value.trim() === '') {

            passwordError.textContent =
                'Enter a password';

            passwordError.style.display =
                'block';


            passwordInput
                .closest('.ev-input-group')
                .classList.add('is-invalid');

        }


        else {

            passwordError.textContent = '';

            passwordError.style.display =
                'none';


            passwordInput
                .closest('.ev-input-group')
                .classList.remove('is-invalid');

        }

    });


    // ==========================================
    // PASSWORD INPUT
    // ==========================================

    passwordInput.addEventListener('input', function () {

        passwordInput
            .closest('.ev-input-group')
            .classList.remove('is-invalid');


        document.getElementById(
            'passwordError'
        ).style.display = 'none';


        if (formErrorAlert) {

            formErrorAlert.classList.add('d-none');

        }

    });


    // ==========================================
    // FORM SUBMISSION
    // ==========================================

    loginForm.addEventListener('submit', function (e) {

        let isValid = true;


        const emailVal =
            emailInput.value.trim();


        const passwordVal =
            passwordInput.value;


        // ======================================
        // EMAIL VALIDATION
        // ======================================

        const emailError =
            document.getElementById('emailError');


        if (!emailVal) {

            emailInput
                .closest('.ev-input-group')
                .classList.add('is-invalid');


            emailError.textContent =
                'Enter an email first';

            emailError.style.display =
                'block';


            isValid = false;

        }


        else if (!isValidEmail(emailVal)) {

            emailInput
                .closest('.ev-input-group')
                .classList.add('is-invalid');


            emailError.textContent =
                'Enter a valid email address';

            emailError.style.display =
                'block';


            isValid = false;

        }


        else {

            emailInput
                .closest('.ev-input-group')
                .classList.remove('is-invalid');


            emailError.style.display =
                'none';

        }


        // ======================================
        // PASSWORD VALIDATION
        // ======================================

        const passwordError =
            document.getElementById('passwordError');


        if (!passwordVal) {

            passwordInput
                .closest('.ev-input-group')
                .classList.add('is-invalid');


            passwordError.textContent =
                'Enter a password';

            passwordError.style.display =
                'block';


            isValid = false;

        }


        else {

            passwordInput
                .closest('.ev-input-group')
                .classList.remove('is-invalid');


            passwordError.style.display =
                'none';

        }


        // ======================================
        // STOP ONLY IF INVALID
        // ======================================

        if (!isValid) {

            e.preventDefault();

            return;

        }


        // ======================================
        // VALID FORM
        // ======================================

        // IMPORTANT:
        // DO NOT use e.preventDefault() here.
        //
        // The browser will now send:
        //
        // POST /login/
        //
        // to Django.


        submitBtn.disabled = true;

        btnText.classList.add('d-none');

        btnSpinner.classList.remove('d-none');

    });

});