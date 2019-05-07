
var origin_url = $('#protected_page').attr("href");

var token = 'bearer '+sessionStorage.getItem("token");

token = window.btoa(token);
var url_with_param = origin_url + '?token=' + token;

$('#protected_page').attr("href", url_with_param);

