$(document).ready(function () {
    const form = $('#resetPasswordForm');
    const newPasswordInput = $('#newPassword');
    const confirmPasswordInput = $('#confirmPassword');
    const submitBtn = $('#submitBtn');
    const btnText = $('#btnText');
    const btnSpinner = $('#btnSpinner');
    const errorAlert = $('#errorAlert');
    const successStateView = $('#successStateView');
    const backToLoginContainer = $('#backToLoginContainer');
    
    // Requirements Elements
    const reqLength = $('#req-length');
    const reqUpper = $('#req-upper');
    const reqLower = $('#req-lower');
    const reqNumber = $('#req-number');
    const strengthBar = $('#strengthBar');
    const strengthText = $('#strengthText');

    // Toggle Password Visibility
    $('.toggle-password').on('click', function () {
        const inputGroup = $(this).closest('.input-group');
        const input = inputGroup.find('input');
        const icon = $(this).find('i');

        if (input.attr('type') === 'password') {
            input.attr('type', 'text');
            icon.removeClass('fa-eye').addClass('fa-eye-slash');
        } else {
            input.attr('type', 'password');
            icon.removeClass('fa-eye-slash').addClass('fa-eye');
        }
    });

    // Real-time Password Strength & Requirements Validation
    newPasswordInput.on('input', function () {
        const val = $(this).val();
        
        let hasLength = val.length >= 8;
        let hasUpper = /[A-Z]/.test(val);
        let hasLower = /[a-z]/.test(val);
        let hasNumber = /[0-9]/.test(val);

        // Update UI checklist
        updateRequirement(reqLength, hasLength);
        updateRequirement(reqUpper, hasUpper);
        updateRequirement(reqLower, hasLower);
        updateRequirement(reqNumber, hasNumber);

        // Calculate strength score (0 to 4)
        let score = 0;
        if (hasLength) score++;
        if (hasUpper) score++;
        if (hasLower) score++;
        if (hasNumber) score++;

        // Update Strength Bar & Label
        if (val.length === 0) {
            strengthBar.css('width', '20%').removeClass('bg-warning bg-success').addClass('bg-danger');
            strengthText.text('Strength: Weak').removeClass('text-warning text-accent').addClass('text-secondary');
        } else if (score <= 2) {
            strengthBar.css('width', '40%').removeClass('bg-success bg-danger').addClass('bg-warning');
            strengthText.text('Strength: Weak').removeClass('text-accent text-secondary').addClass('text-warning');
        } else if (score === 3) {
            strengthBar.css('width', '75%').removeClass('bg-danger bg-warning').addClass('bg-warning');
            strengthText.text('Strength: Medium').removeClass('text-warning text-secondary').addClass('text-warning');
        } else {
            strengthBar.css('width', '100%').removeClass('bg-danger bg-warning').addClass('bg-success');
            strengthText.text('Strength: Strong').removeClass('text-warning text-secondary').addClass('text-accent');
        }

        // Validate confirmation match if confirm field is not empty
        if (confirmPasswordInput.val().length > 0) {
            validateConfirmPassword();
        }
    });

    function updateRequirement(element, isValid) {
        const icon = element.find('i');
        if (isValid) {
            element.addClass('valid text-accent');
            icon.removeClass('fa-regular fa-circle text-secondary').addClass('fa-solid fa-circle-check text-accent');
        } else {
            element.removeClass('valid text-accent');
            icon.removeClass('fa-solid fa-circle-check text-accent').addClass('fa-regular fa-circle text-secondary');
        }
    }

    // Confirm Password Real-time Check
    confirmPasswordInput.on('input', function () {
        validateConfirmPassword();
    });

    function validateConfirmPassword() {
        const pass = newPasswordInput.val();
        const confirmPass = confirmPasswordInput.val();

        if (confirmPass.length === 0) {
            confirmPasswordInput.removeClass('is-valid is-invalid');
            $('#confirmPasswordSuccess').hide();
            return false;
        }

        if (pass === confirmPass) {
            confirmPasswordInput.removeClass('is-invalid').addClass('is-valid');
            $('#confirmPasswordSuccess').show();
            return true;
        } else {
            confirmPasswordInput.removeClass('is-valid').addClass('is-invalid');
            $('#confirmPasswordSuccess').hide();
            return false;
        }
    }

    // Form Submission Handler
    form.on('submit', function (e) {
        e.preventDefault();

        const pass = newPasswordInput.val();
        const confirmPass = confirmPasswordInput.val();

        // Reset error banner
        errorAlert.addClass('d-none');
        newPasswordInput.removeClass('is-invalid');
        confirmPasswordInput.removeClass('is-invalid');

        let isValid = true;
        let errorMessage = "Please fix the highlighted errors below.";

        // Validation logic
        if (!pass) {
            newPasswordInput.addClass('is-invalid');
            $('#newPasswordError').text('New password is required.');
            isValid = false;
        } else if (pass.length < 8) {
            newPasswordInput.addClass('is-invalid');
            $('#newPasswordError').text('Password must contain at least 8 characters.');
            isValid = false;
        } else if (!/[A-Z]/.test(pass)) {
            newPasswordInput.addClass('is-invalid');
            $('#newPasswordError').text('Password must contain at least one uppercase letter.');
            isValid = false;
        } else if (!/[a-z]/.test(pass)) {
            newPasswordInput.addClass('is-invalid');
            $('#newPasswordError').text('Password must contain at least one lowercase letter.');
            isValid = false;
        } else if (!/[0-9]/.test(pass)) {
            newPasswordInput.addClass('is-invalid');
            $('#newPasswordError').text('Password must contain at least one number.');
            isValid = false;
        }

        if (pass !== confirmPass) {
            confirmPasswordInput.addClass('is-invalid');
            $('#confirmPasswordError').text('Passwords do not match.');
            isValid = false;
        }

        if (!isValid) {
            $('#errorMessageText').text(errorMessage);
            errorAlert.removeClass('d-none');
            return;
        }

        // Trigger Loading State (Simulated secure token validation and Django backend save)
        submitBtn.prop('disabled', true);
        btnText.text('Resetting Password...');
        btnSpinner.removeClass('d-none');
        newPasswordInput.prop('disabled', true);
        confirmPasswordInput.prop('disabled', true);

        setTimeout(() => {
            // Reset button state
            submitBtn.prop('disabled', false);
            btnText.text('Reset Password');
            btnSpinner.addClass('d-none');

            // Hide form and show success state
            form.addClass('d-none');
            successStateView.removeClass('d-none');
            backToLoginContainer.addClass('d-none');

        }, 1400);
    });
});