var sessions = $('#session-datatable').DataTable( {
    "pageLength": 15,
    "lengthMenu": [[15, 25, 50, -1], [15, 25, 50, "All"]],
    "ajax": {
            "type" : "GET",
            "url" : "/api/session",
            "dataSrc": function ( json ) {
                console.log(json)
                return json;
            }
            },
    "columns": [
                    { "data": "user_name" },
                    { "data": "calling_station_id",
                        "render": function (data, type, row, meta) {
                            mac = row.calling_station_id
                            var url = '<a href="/session/MACAddress/' + mac + '">' + mac + '</a>'
                            console.log(url)
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
setInterval( function () {
    sessions.ajax.reload();
}, 10000 );
