$("form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api/token/",
        data: $(this).serialize(),
        success: function (data) {
            localStorage.setItem('jwt_token', data.access);
            localStorage.setItem('jwt_token_refresh', data.refresh);
            window.location.href = "http://127.0.0.1:8000/account/";
        }
    });
});