var csrftoken = getCookie('csrftoken');
var token = localStorage.getItem("token");

function colorchange(ele) {
    var background = ele.style.backgroundColor;
    if (background == "rgb(133, 193, 233)") {
        ele.style.background = "rgb(52, 152, 219)";//like
    } else {
        ele.style.background = "rgb(133, 193, 233)";//unlike
    }

    var p_node=ele.parentNode ;
    var post_id = $(p_node).parents("tr").find('input[name="post_id"]').val()

     var data = {
            "post_id": post_id,
            "token": token
        };
        data = JSON.stringify(data);
        $.ajax({
            url: "/like/",
            type: "POST",
            contentType: 'application/json; charset=utf-8',
            dataType: 'text',
            data: data,
            success: function(response) {
                response = JSON.parse(response);
                if (response.statusCode == 200) {
                    var like_details = response.like_details;
                    var likes_name_list = ""
                    for(var i=0;i<like_details.likes_name.length;i++){
                        likes_name_list += '<li>'+like_details.likes_name[i]+'</li>'
                     }
                      tmp = like_details.likes+'<ul class="list-categories">'+likes_name_list+'</ul>'
                      var row_no=ele.parentNode ;
                      $(row_no).parents("tr").find("a").html(tmp);

                } else if (response.statusCode == 404) {
                    console.log("something went wrong in PostSubmit Api StatusCode : " + response.statusCode);
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


$("#post-btn").click(function () {
    var content = $('#post').val();
    var title = $('#title').val();
    if (typeof(title) == "undefined" || title == ""){
        alert('This post appears to be blank title. Please write title.');
    }
    else if (typeof(content) == "undefined" || content == ""){
        alert('This post appears to be blank. Please write something.');
    }
    else{
        $("textarea#post").val("");
        $("input#title").val("");


        var data = {
            "title": title,
            "content": content,
            "token": token
        };
        data = JSON.stringify(data);
        $.ajax({
            url: "/save_new_post/",
            type: "POST",
            contentType: 'application/json; charset=utf-8',
            dataType: 'text',
            data: data,
            success: function(response) {
                response = JSON.parse(response);
                if (response.statusCode == 200) {
                    var post_details = response.post_details;
                    var likes_name_list = ""
                    for(var i=0;i<post_details.likes_name.length;i++){
                        likes_name_list += '<li>'+post_details.likes_name[i]+'</li>'
                     }
                    var tmp = '<tr><td><input type="text" name="post_id" value='+post_details.post_id+' style="display:none;" readonly/>'
                    tmp += '<h4><strong>'+title+'</strong></h4>'
                    tmp += '<p>posted by:'+post_details.author+','+post_details.publish_time+'</p>'+content+'<br>'
                    tmp += '<button type="button" class="like" onclick="colorchange(this);" style="background:rgb(133, 193, 233);">'
                    tmp += '<span class="glyphicon glyphicon-thumbs-up"></span>'
                    tmp += '</button>'
                    tmp+= '<a class="like-list"> '+ post_details.likes
                    tmp+= '<ul class="list-categories">'+likes_name_list+'</ul>'
                    tmp += '</a></td></tr>';
                    tmp = $(tmp);
                    $('#content_list').prepend(tmp);
                } else if (response.statusCode == 404) {
                    console.log("something went wrong in PostSubmit Api StatusCode : " + response.statusCode);
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