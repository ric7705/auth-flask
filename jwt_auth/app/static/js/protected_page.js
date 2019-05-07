$.ajax({
    type: 'GET',
    contentType: "application/json; charset=utf-8",
    url: '/api/get_members',
    dataType: 'json',
    beforeSend: function(xhr) {
        var token = sessionStorage.getItem("access_token");
        xhr.setRequestHeader("Authorization", "Bearer " + token);
    },
    success: function(res) {
        console.log(res);
        if(res.status=='success'){
            res.members.forEach(function(item, index, array){
                $("#members ol").append('<li>'+item.username+'</li>');
                console.log(item, index, array);
            });
        }
    },
    error: function(error) {
        console.log(error);
        // window.location = '/login';
    }
});
