$("form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api-token-auth/",
        data: $(this).serialize(),
        success: function (data) {
            localStorage.setItem('jwt_token', data.token);
            window.location.href = "http://127.0.0.1:8000/account/";
        }
    });
});