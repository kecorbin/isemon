var sessions = $('#session-datatable').DataTable( {
    "ajax": {
            "type" : "GET",
            "url" : "/api/session",
            "dataSrc": function ( json ) {
                console.log(json)
                return json;
            }
            },

    "columns": [
                    { "data": "audit_session_id" },
                    { "data": "calling_station_id" },
                    { "data": "user_name"},
                    { "data": "nas_ip_address"},
                    { "data": "server"}
                ]
    }
);


// auto refresh the datatable
setInterval( function () {
    sessions.ajax.reload();
}, 10000 );
