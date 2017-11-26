# encoding=utf8
from flask import Flask, render_template, request
# from flask_restful import Api

from isemon.views.session import session_list, session_detail
from isemon.views.patterns import patterns
from isemon.views.authstatus import authstatus_history, authstatus_search
from isemon.views.apidocs import swagger_ui

from isemon.api.session import (ActiveSessionCount,
                                ActiveSessionList, AuthenticatedSessionList,
                                SessionDetailByMAC, SessionDetailByIP,
                                SessionDetailByUser, SessionDetailByNAS)

from isemon.api.troubleshooting import AuthStatus, FailureReason

from flask_restful_swagger_2 import swagger, Api

app = Flask(__name__)

api = Api(app,
          api_version='0.1',
          title="Maverick",
          api_spec_url='/api/swagger',
          description="Maverick API for Cisco Identity Services Engine"
          )


@app.route('/')
def index():
    return render_template('index.html')

# session endpoints
api.add_resource(ActiveSessionList, '/api/session')
api.add_resource(ActiveSessionCount, '/api/session-count')
api.add_resource(SessionDetailByMAC, '/api/session/MACAddress/<string:mac_address>')
api.add_resource(SessionDetailByIP, '/api/session/IPAddress/<string:ip_address>')
api.add_resource(SessionDetailByUser, '/api/session/UserName/<string:user_name>')
api.add_resource(SessionDetailByNAS, '/api/session/UserName/<string:nas_ip_address>')

# troubleshooting endpoints
api.add_resource(AuthStatus, '/api/authstatus',
                             '/api/authstatus/<string:mac_address>',
                             '/api/authstatus/<string:mac_address>/<string:duration>',
                             '/api/authstatus/<string:mac_address>/<string:duration>/<string:num_records>',
                             '/api/authstatus/<string:mac_address>/<string:duration>/<string:num_records>/<string:verbosity>')
api.add_resource(FailureReason, '/api/failurereason')



# web views
app.add_url_rule('/session', endpoint='session-list', view_func=session_list)
app.add_url_rule('/session/MACAddress/<string:mac_address>', view_func=session_detail)
# app.add_url_rule('/history/MACAddress/<string:mac_address>',
#                  endpoint='session-history-results',
#                  view_func=authstatus_history)
app.add_url_rule('/history/', endpoint="session-history", methods=["GET", "POST"], view_func=authstatus_search)
app.add_url_rule('/patterns', endpoint='patterns', view_func=patterns)
app.add_url_rule('/apidocs', endpoint='api-docs', view_func=swagger_ui)

if __name__ == '__main__':
    app.secret_key = "dktm872xl2sxx9vmelSFJ2jsLEEFLx"
    app.run(host='127.0.0.1', port=5000, debug=True)
