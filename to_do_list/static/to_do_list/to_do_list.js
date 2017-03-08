$(document).ready(function() {

    //csrftoken setup
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue =
                    decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        //these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFTOKEN", csrftoken);
            }
        }
    });
    //end csrftoken setup

    //include jQuery-ui's sortable widget
    $("#tasklist").sortable({
      placeholder: "sortable-placeholder"
    })
    .on("sortupdate", function(event, ui){
      //set taskid and movedto location
      var taskid = ui.item.attr('data-id')
      var tasklist = ui.item.attr('data-tasklist')
      var movedto = parseInt(ui.item.index()) + 1

      //submit updated item to server
      $.ajax("/todolist/" + tasklist + "/reorder/", {
        type: 'POST',
        dataType: 'json',
        data: {
          taskid: taskid,
          movedto: movedto
        }
      })

      //change priority clientside
      $(".task").each(function() {
        $(this).attr("data-priority", ($(this)[0].rowIndex))
        $(this).children().filter(".priority").text(($(this)[0].rowIndex))
      });
    });

    //delete task
    $(".deletetaskbutton").click(function() {
        var taskid = ($(this).parent().parent()[0].getAttribute('data-id'))
        $.ajax({
          url: "delete/" + taskid + "/",
          type: 'DELETE'
        })
        location.reload();
      });

});
