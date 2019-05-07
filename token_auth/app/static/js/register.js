function register() {
    var payload = {};
    payload['username'] = $('#username').val();
    payload['password'] = $('#password').val();

    console.log(payload);

    $.ajax({
        type: 'POST',
        contentType: "application/json; charset=utf-8",
        url: '/api/register',
        data: JSON.stringify(payload),
        dataType: 'json',

        success: function(payload) {
            console.log(payload);
            alert("Successful");
            window.location = '/';
        },
        error: function(error) {
            console.log(error);
            alert("Fail");
        }
    });
}