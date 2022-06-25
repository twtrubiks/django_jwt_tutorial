$("form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/auth/users/",
        data: $(this).serialize(),
        success: function () {
            window.location.href = "http://127.0.0.1:8000/account/login/";
        },
        error: function (data) {
            console.log(data.responseText)
        }
    });
});