let departments = []; 

$.getJSON("/registration/alldepartments", function(data) {
            $.each(data, function(key, val) {
                $("#department").append("<option value='" + val.id + "'>" + val.name + "</option>");
            });
            departments = data;
        });