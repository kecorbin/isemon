var sessions = $('#session-datatable').DataTable( {
    "pageLength": 15,
    "lengthMenu": [[15, 25, 50, -1], [15, 25, 50, "All"]],
    'language': {
      "processing": '<div class="loading-dots loading-dots--muted"><span></span><span></span><span></span></div>'
    },

    "ajax": {
            "type" : "GET",
            "url" : "/api/session",
            "timeout": 60,
            "dataSrc": function ( json ) {
                return json;
            }
            },
    "columns": [
                    { "data": "user_name" },
                    { "data": "calling_station_id",
                        "render": function (data, type, row, meta) {
                            mac = row.calling_station_id
                            var url = '<a href="/session/MACAddress/' + mac + '">' + mac + '</a>'
                              return url
                        }
                    },

                    { "data": "framed_ip_address"},
                    { "data": "nas_ip_address"},
                    { "data": "server"}
                ]
    }
);


// auto refresh the datatable
// setInterval( function () {
//     sessions.ajax.reload();
// }, 10000 );
