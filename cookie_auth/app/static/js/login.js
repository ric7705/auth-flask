function login() {
    var payload = {};
    payload['username'] = $('#username').val();
    payload['password'] = $('#password').val();

    console.log(payload);

    $.ajax({
        type: 'POST',
        contentType: "application/json; charset=utf-8",
        url: '/api/login',
        data: JSON.stringify(payload),
        dataType: 'json',
        success: function(res) {

            if(res.status === 'success'){
                console.log(res);
                alert("Successful");
                window.location = '/';
            }else{
                alert("Fail");

            }
        },
        error: function(error) {
            console.log(error);
            alert("Fail");
        }
    });
}