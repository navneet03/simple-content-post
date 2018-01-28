var csrftoken = getCookie('csrftoken');


$("#signIn_Submit").click(function () {
     var email = $('#email').val();
    var password = $('#password').val();

    if ((typeof(email) == "undefined" || email == "") || (typeof(password) == "undefined" || password == "")) {
        alert("Please Enter the all Input Form Value");
    } else if (!(validateEmail(email))) {
        alert('Please Enter Valid E-Mail');
    } else {
        var data = {
            "email": email,
            "password": password,
        };
        data = JSON.stringify(data);
        $.ajax({
            url: "/login/",
            type: "POST",
            contentType: 'application/json; charset=utf-8',
            dataType: 'text',
            data: data,
            success: function(response) {
                response = JSON.parse(response);
                if (response.statusCode == 200) {
                    localStorage.setItem("token", response.token);
                     window.location = '/home/';
                } else if (response.statusCode == 404) {
                    console.log("something went wrong in LogIn Api StatusCode : " + response.statusCode);
                } else {
                    alert(response.data);
                }
            },

            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
    }
});

$("#signUp_Submit").click(function () {
    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var email = $('#signup_email').val();
    var password = $('#signup_password').val();
    var re_password = $('#re_password').val();
    var phone_no = $('#phone').val();
    var gender = $('#gender').val();


    if ((typeof(first_name) == "undefined" || first_name == "") || (typeof(password) == "undefined" || password == "") ||
        (typeof(re_password) == "undefined" || re_password == "") || (typeof(email) == "undefined" || email == "") ||
        (typeof(phone_no) == "undefined" || phone_no == "")) {
        alert("Please Enter the all Input Form Value");
    } else if (!(validateEmail(email))) {
        alert('Please Enter Valid E-Mail');
    } else if (password.length < 6) {
        alert("Password must have at least 6 character ");
    } else if (password != re_password) {
        alert("Your Password and Re-Enter Password do not match.");
    } else {
        var data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "re_password": password,
            "phone_no": phone_no,
            "gender": gender,
        };
        data = JSON.stringify(data);
        $.ajax({
            url: "/save_signup_info/",
            type: "POST",
            contentType: 'application/json; charset=utf-8',
            dataType: 'text',
            data: data,
            success: function(response) {
                response = JSON.parse(response);
                if (response.statusCode == 200) {
                    localStorage.setItem("token", response.token);
                    window.location = '/home/';
                } else if (response.statusCode == 404) {
                    console.log("something went wrong in SignUp Api StatusCode : " + response.statusCode);
                } else {
                    alert(response.data);
                }
            },

            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
    }
});

//validate email address
function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

//For getting CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}