$( document ).ready(function() {
	$("#editRecInfo").click(function(){
        $.ajax({
            url: '/getRec',
            data: {
            companyName: 'cName',
            },
            type: 'POST',
            success: function(response){
            var result = $.parseJSON(response);
            $.each(result["companyDetails"], function (index, value) {
                $('#companyD').append('<tr><td id="'+value[1]+'" class="editCompany">'+value[0]+'</td></tr>');
            });
            },
            error: function(error){
            console.log(error);
            }
        });
    });
});