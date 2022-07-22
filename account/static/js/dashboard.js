var jwt_token = localStorage.getItem('jwt_token');
var jwt_token_refresh = localStorage.getItem('jwt_token_refresh');
data = {
    "refresh": jwt_token_refresh
};
$.ajax({
    type: "POST",
    url: "http://127.0.0.1:8000/api/token/refresh/",
    data: data,
    success: function (data) {
        localStorage.setItem('jwt_token', data.access_token);
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/api/musics/",
            headers: {
                "Authorization": "Bearer" + " " + localStorage.getItem('jwt_token')
            },
            success: function (data) {
                var result = "";
                for (var i in data) {
                    result += data[i].id + ", " + data[i].song + " , " + data[i].singer + "-----";
                }
                $("#result").text(result).css('color', 'blue');
            },
            error: function (data) {
                var result = "please login " + data.responseText;
                $("#result").text(result).css('color', 'red');
            }
        });
    },
    error: function (data) {
        var result = "please login " + data.responseText;
        $("#result").text(result).css('color', 'red');
    }
});