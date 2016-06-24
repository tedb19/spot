
(function(){

    $(document).ready(function() {
        autoCloseAlert(".alert");
        initializeFormset('#formset tbody tr');
    });


    function autoCloseAlert(selector){
        $(selector).fadeTo(2000, 500).slideUp(2000, function(){
            $(selector).alert('close');
        });
    }

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

    function initializeFormset(selector){
        $(selector).formset({
            addText: '<i class="fa fa-plus-square" data-toggle="tooltip" data-placement="right" title="add more properties"></i>',
            deleteText: '<i class="fa fa-times" data-toggle="tooltip" data-placement="right" title="delete row"></i>'
        });
    }



    $('.modal').on('shown.bs.modal', function () {
        var pk = $(this).find('.pk').text();
        $.ajax({
              type: "POST",
              url: '/project-resources/get_resource_properties/',
              data: "resource_id="+pk,
              headers: {"X-CSRFToken": getCookie('csrftoken')},
              dataType: 'json',
              success: function (data) {
                $(".resultset").find('tbody tr').remove();
                var resource_properties = data.data;
                for(var i = 0; i < resource_properties.length;  i++){
                    var property = resource_properties[i];
                    var newRow = '<tr class="odd gradeX"><td><b>'+property.name+'</b></td><td>'+property.value+'</td></tr>';

                    $('.in').find('tbody').append(newRow);
                }
              }
        });
    })

    /*
    * Checks if an element selected exists
    */
    $.fn.exists = function () {
        return this.length !== 0;
    }

}());
