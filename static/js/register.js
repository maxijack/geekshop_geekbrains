
$("#reg_form").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(), // serializes the form's elements.
        success: function(resp)
        {
            message = 'сообщение для подтверждения регистрации отправлено, код: ' + resp
            $("#liveAlertPlaceholder").append('<div class="alert alert-success alert-dismissible" role="alert">' + message + '</div>')
        }
    });
    
});