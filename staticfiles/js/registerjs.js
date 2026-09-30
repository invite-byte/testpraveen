document.addEventListener('DOMContentLoaded', function () {
    const registerForm = document.getElementById('evRegisterForm');
    const nameInput = document.getElementById('id_fullname');
    const mobileInput = document.getElementById('id_mobile');
    const emailInput = document.getElementById('id_email');
    const passwordInput = document.getElementById('id_password');
    const confirmPasswordInput = document.getElementById('id_confirm_password');
    const termsCheckbox = document.getElementById('id_terms');
    
    const togglePasswordBtn = document.getElementById('togglePassword');
    const togglePasswordIcon = document.getElementById('togglePasswordIcon');
    const toggleConfirmPasswordBtn = document.getElementById('toggleConfirmPassword');
    const toggleConfirmPasswordIcon = document.getElementById('toggleConfirmPasswordIcon');
    
    const submitBtn = document.getElementById('registerSubmitBtn');
    const btnText = submitBtn.querySelector('.btn-text');
    const btnSpinner = submitBtn.querySelector('.btn-spinner');
    const formErrorAlert = document.getElementById('formErrorAlert');
    const formErrorText = document.getElementById('formErrorText');
    const successStateContainer = document.getElementById('successStateContainer');
    
    const strengthBar = document.getElementById('strengthBar');
    const strengthText = document.getElementById('strengthText');

    // 1. Password Visibility Toggles
    togglePasswordBtn.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        togglePasswordIcon.className = type === 'text' ? 'fa-regular fa-eye-slash' : 'fa-regular fa-eye';
    });

    toggleConfirmPasswordBtn.addEventListener('click', function () {
        const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        confirmPasswordInput.setAttribute('type', type);
        toggleConfirmPasswordIcon.className = type === 'text' ? 'fa-regular fa-eye-slash' : 'fa-regular fa-eye';
    });

    // 2. Real-time Password Strength Meter Calculation
    passwordInput.addEventListener('input', function() {
        const val = passwordInput.value;
        let score = 0;

        if (val.length >= 8) score++;
        if (/[A-Z]/.test(val)) score++;
        if (/[a-z]/.test(val)) score++;
        if (/[0-9]/.test(val)) score++;

        if (val.length === 0) {
            strengthBar.style.width = '0%';
            strengthBar.className = 'progress-bar transition-all';
            strengthText.textContent = 'Weak';
            strengthText.style.color = '#94a3b8';
        } else if (score <= 2) {
            strengthBar.style.width = '33%';
            strengthBar.className = 'progress-bar bg-danger transition-all';
            strengthText.textContent = 'Weak';
            strengthText.style.color = '#ef4444';
        } else if (score === 3) {
            strengthBar.style.width = '66%';
            strengthBar.className = 'progress-bar bg-warning transition-all';
            strengthText.textContent = 'Medium';
            strengthText.style.color = '#f59e0b';
        } else {
            strengthBar.style.width = '100%';
            strengthBar.className = 'progress-bar bg-success transition-all';
            strengthText.textContent = 'Strong';
            strengthText.style.color = '#00ff88';
        }
    });

    // Restrict mobile input to numbers only
    mobileInput.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '').slice(0, 10);
    });

    // Helper Validators
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    function isValidMobile(mobile) {
        return /^[6-9]\d{9}$/.test(mobile); // Standard Indian mobile number validator format
    }

    // Clear validation state on interaction
    const inputs = [nameInput, mobileInput, emailInput, passwordInput, confirmPasswordInput];
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            input.closest('.ev-input-group').classList.remove('is-invalid');
            const errorElement = document.getElementById(input.id.replace('id_', '') + 'Error') || document.getElementById(input.id === 'id_confirm_password' ? 'confirmPasswordError' : '');
            if (errorElement) errorElement.style.display = 'none';
            formErrorAlert.classList.add('d-none');
        });
    });

    termsCheckbox.addEventListener('change', function() {
        document.getElementById('termsError').style.display = 'none';
    });

    // 3. Form Submission & Validation UX Handling
    registerForm.addEventListener('submit', function (e) {
        let isValid = true;
        const nameVal = nameInput.value.trim();
        const mobileVal = mobileInput.value.trim();
        const emailVal = emailInput.value.trim();
        const passwordVal = passwordInput.value;
        const confirmPasswordVal = confirmPasswordInput.value;

        formErrorAlert.classList.add('d-none');

        // Full Name Validation
        if (!nameVal || nameVal.length < 2) {
            nameInput.closest('.ev-input-group').classList.add('is-invalid');
            document.getElementById('nameError').style.display = 'block';
            isValid = false;
        }

        // Mobile Number Validation
        if (!isValidMobile(mobileVal)) {
            mobileInput.closest('.ev-input-group').classList.add('is-invalid');
            document.getElementById('mobileError').style.display = 'block';
            isValid = false;
        }

        // Email Validation
        if (!isValidEmail(emailVal)) {
            emailInput.closest('.ev-input-group').classList.add('is-invalid');
            document.getElementById('emailError').style.display = 'block';
            isValid = false;
        }

        // Password Complexity Requirements Validation
        const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
        if (!passRegex.test(passwordVal)) {
            passwordInput.closest('.ev-input-group').classList.add('is-invalid');
            document.getElementById('passwordError').style.display = 'block';
            isValid = false;
        }

        // Confirm Password Match Validation
        if (passwordVal !== confirmPasswordVal || !confirmPasswordVal) {
            confirmPasswordInput.closest('.ev-input-group').classList.add('is-invalid');
            document.getElementById('confirmPasswordError').style.display = 'block';
            isValid = false;
        }

        // Terms Agreement Validation
        if (!termsCheckbox.checked) {
            document.getElementById('termsError').style.display = 'block';
            isValid = false;
        }

        if (!isValid) {
            formErrorText.textContent = 'Please correct the highlighted fields before continuing.';
            formErrorAlert.classList.remove('d-none');
            return;
        }

        // 4. Loading State Simulation (Ready for Django Backend POST / AJAX)
        submitBtn.setAttribute('disabled', 'true');
        btnText.classList.add('d-none');
        btnSpinner.classList.remove('d-none');

        // Simulating backend request & success response flow
        setTimeout(() => {
            // Hide registration form card content and reveal success state
            registerForm.classList.add('d-none');
            successStateContainer.classList.remove('d-none');
            
            // Future Integration Flow: Automatically redirect or present dashboard link
            // window.location.href = '/dashboard/my-garage/';
        }, 1500);
    });
});