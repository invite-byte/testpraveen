document.addEventListener("DOMContentLoaded", function () {

    // -----------------------------------------
    // ELEMENTS
    // -----------------------------------------

    const forgotForm = document.getElementById("forgotPasswordForm");

    const otpView = document.getElementById("successStateView");

    const newPasswordView = document.getElementById("newPasswordView");

    const emailInput = document.getElementById("email");

    const otpInput = document.getElementById("verificationCode");

    const otpForm = document.getElementById("otpForm");

    const newPasswordForm = document.getElementById("newPasswordForm");

    const submitBtn = document.getElementById("submitBtn");

    const btnText = document.getElementById("btnText");

    const btnSpinner = document.getElementById("btnSpinner");

    const verifyBtn = document.getElementById("verifyCodeBtn");

    const verifyBtnText = document.getElementById("verifyBtnText");

    const verifySpinner = document.getElementById("verifySpinner");

    const resendBtn = document.getElementById("resendCodeBtn");

    const backToLogin = document.getElementById("backToLoginContainer");


    // -----------------------------------------
    // OTP INPUT
    // Only numbers
    // -----------------------------------------

    if (otpInput) {

        otpInput.addEventListener("input", function () {

            this.value = this.value.replace(/\D/g, "");

            if (this.value.length > 6) {
                this.value = this.value.slice(0, 6);
            }

        });

    }


    // -----------------------------------------
    // SEND OTP BUTTON
    // -----------------------------------------

    if (forgotForm) {

        forgotForm.addEventListener("submit", function () {

            if (!emailInput.value.trim()) {
                return;
            }

            submitBtn.disabled = true;

            btnText.textContent = "Sending Code...";

            btnSpinner.classList.remove("d-none");

        });

    }


    // -----------------------------------------
    // OTP FORM
    // -----------------------------------------

    // if (otpForm) {

    //     otpForm.addEventListener("submit", function () {

    //         const otp = otpInput.value.trim();

    //         if (otp.length !== 6) {

    //             otpInput.classList.add("is-invalid");

    //             return;

    //         }

    //         otpInput.classList.remove("is-invalid");

    //         verifyBtn.disabled = true;

    //         verifyBtnText.textContent = "Verifying...";

    //         verifySpinner.classList.remove("d-none");

    //     });

    // }


    // -----------------------------------------
    // RESEND OTP
    // -----------------------------------------

    // if (resendBtn) {

    //     resendBtn.addEventListener("click", function () {

    //         if (!emailInput) {
    //             return;
    //         }

    //         const email = emailInput.value;

    //         if (!email) {
    //             return;
    //         }

    //         // Create a new form
    //         const form = document.createElement("form");

    //         form.method = "POST";

    //         form.action = window.location.href;

    //         // CSRF
    //         const csrf = document.querySelector(
    //             "[name=csrfmiddlewaretoken]"
    //         );

    //         if (csrf) {

    //             const csrfInput = document.createElement("input");

    //             csrfInput.type = "hidden";

    //             csrfInput.name = "csrfmiddlewaretoken";

    //             csrfInput.value = csrf.value;

    //             form.appendChild(csrfInput);

    //         }


    //         // Action
    //         const actionInput = document.createElement("input");

    //         actionInput.type = "hidden";

    //         actionInput.name = "action";

    //         actionInput.value = "send_otp";

    //         form.appendChild(actionInput);


    //         // Email
    //         const emailField = document.createElement("input");

    //         emailField.type = "hidden";

    //         emailField.name = "email";

    //         emailField.value = email;

    //         form.appendChild(emailField);


    //         document.body.appendChild(form);

    //         form.submit();

    //     });

    // }


    // -----------------------------------------
    // PASSWORD MATCH CHECK
    // -----------------------------------------

    // if (newPasswordForm) {

    //     newPasswordForm.addEventListener("submit", function (event) {

    //         const password =
    //             document.getElementById("newPassword").value;

    //         const confirmPassword =
    //             document.getElementById("confirmPassword").value;


    //         if (password !== confirmPassword) {

    //             event.preventDefault();

    //             alert("Passwords do not match.");

    //             return;

    //         }


    //         if (password.length < 8) {

    //             event.preventDefault();

    //             alert("Password must contain at least 8 characters.");

    //             return;

    //         }

    //     });

    // }

});