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
    $("#tasklist").sortable()
        .on("sortupdate", function(event, ui){
          //set droppedItem, nextItem, and previousItem
          droppedItem = ui.item
          droppedItemPriority = droppedItem.attr('data-priority')
          droppedItemPosition = parseInt(droppedItem.index())+1
          previousItem = ui.item.prev()[0]
          nextItem = ui.item.next()[0]

          //submit updated item to server
          $.ajax("/todolist/reorder/", {
            type: 'POST',
            dataType: 'json',
            data: {
              droppedItemPriority: droppedItemPriority,
              droppedItemPosition: droppedItemPosition,
              previousItemPriority: previousItem &&
              previousItem.getAttribute('data-priority'),
              nextItemPriority: nextItem &&
              nextItem.getAttribute('data-priority')
            }
          })

          //change priority clientside
          $(".task").each(function() {
            $(this).attr("data-priority", ($(this)[0].rowIndex +1))
            $(this).children().filter(".priority").text("PRIORITY: " + ($(this)[0].rowIndex +1))
          });
        });

    //begin working on task
    $(".workontask").click(function() {
        var tasktext = $(this).parent().parent().children(".taskname").text()
        $("#currenttask").text(tasktext)
        console.log($("#taskstartedtime").text($.now()))
        //$("#taskstartedtime").text($now())
      });


    //delete task
    $(".deletetask").click(function() {
        var taskid = ($(this).parent().parent()[0].getAttribute('data-id'))
        $.ajax({
          url: "delete/" + taskid + "/",
          type: 'DELETE'
        })
        location.reload();
      });

});
