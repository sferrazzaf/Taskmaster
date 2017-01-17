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
          console.log(droppedItem)
          droppedItemPriority = droppedItem.attr('data-priority')
          console.log("droppedItemPriority = " + droppedItemPriority)
          droppedItemPosition = parseInt(droppedItem.index())+1
          console.log("droppedItemPosition = " + droppedItemPosition)
          previousItem = ui.item.prev()[0]
          nextItem = ui.item.next()[0]

          //change priority clientside

          //submit updated item to server
          $.ajax("/todolist/reorder/", {
            type: 'POST',
            dataType: 'json',
            data: {
              droppedItemPriority: droppedItemPriority,
              droppedItemPosition: droppedItemPosition,
              previousItemPosition: previousItem && previousItem.rowIndex+1,
              previousItemPriority: previousItem &&
              previousItem.getAttribute('data-priority'),
              nextItemPosition: nextItem && nextItem.rowIndex + 1,
              nextItemPriority: nextItem &&
              nextItem.getAttribute('data-priority')
            }
          })
        });

    $(".deletetask").click(function() {
        var taskid = ($(this).parent().parent()[0].getAttribute('data-id'))
        $.ajax({
          url: "delete/" + taskid + "/",
          type: 'DELETE'
        })
        location.reload();
      });

});
