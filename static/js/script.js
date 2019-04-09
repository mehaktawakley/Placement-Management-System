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

    $(document).on('click', '.editCompany', function(){ 
        var id = $(this).attr('id');
        console.log(id);
        $.ajax({
            url: '/getRecDetails',
            data: {
            cID: $(this).attr('id')
            },
            type: 'POST',
            success: function(response){
            var result = $.parseJSON(response);
            $("#eventModalLabel").val(result["companyDetails"][0]);
            $("textarea#aboutComapny").text(result["companyDetails"][1]);
            $("#roleOff").val(result["companyDetails"][2]);
            $("#compEligibility").val(result["companyDetails"][3]);
            $("#compLoc").val(result["companyDetails"][4]);
            $("#salaryOffered").val(result["companyDetails"][5]);
            $("#edWE").text(result["companyDetails"][6]);
            $("#rolesResp").text(result["companyDetails"][7]);
            $("#cId").val(id);
            },
            error: function(error){
            console.log(error);
            }
        });
        $('#companyModal').modal('show');
    });

    $(document).on('click', '#remCompany', function(){ 
        var id = $('#cId', $(this).closest("div.modal-body")).val();
        console.log(id);
        $.ajax({
            url: '/remRec',
            data: {
            cID: $('#cId', $(this).closest("div.modal-body")).val()
            },
            type: 'POST',
            success: function(response){
                console.log("success");
                $('#'+id).remove();
            },
            error: function(error){
            console.log(error);
            }
        });
    });

    $(document).on('click', '#editComp', function(){ 
        var cName = $('#eventModalLabel', $(this).closest("div.modal-body")).val();
        var aboutComapny = $('#aboutComapny', $(this).closest("div.modal-body")).text();
        var role = $('#roleOff', $(this).closest("div.modal-body")).val();
        var eligibility = $('#compEligibility', $(this).closest("div.modal-body")).val();
        var compLoc = $('#compLoc', $(this).closest("div.modal-body")).val();
        var salaryOffered = $('#salaryOffered', $(this).closest("div.modal-body")).val();
        var edWE = $('#edWE', $(this).closest("div.modal-body")).val();
        var rolesResp = $('#rolesResp', $(this).closest("div.modal-body")).val();
        var id = $('#cId', $(this).closest("div.modal-body")).val();
        $.ajax({
            url: '/updateRec',
            data: {
                cName : $('#eventModalLabel', $(this).closest("div.modal-body")).val(),
                aboutComapny : $('#aboutComapny', $(this).closest("div.modal-body")).text(),
                role : $('#roleOff', $(this).closest("div.modal-body")).val(),
                eligibility : $('#compEligibility', $(this).closest("div.modal-body")).val(),
                compLoc : $('#compLoc', $(this).closest("div.modal-body")).val(),
                salaryOffered : $('#salaryOffered', $(this).closest("div.modal-body")).val(),
                edWE : $('#edWE', $(this).closest("div.modal-body")).val(),
                rolesResp : $('#rolesResp', $(this).closest("div.modal-body")).val(),
                id : $('#cId', $(this).closest("div.modal-body")).val()
            },
            type: 'POST',
            success: function(response){
                console.log("success");
            },
            error: function(error){
            console.log(error);
            }
        });
    });

});