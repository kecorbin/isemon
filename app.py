# encoding=utf8
from flask import Flask, render_template, request
from flask_restful import Api
from views.session import session_list
from views.patterns import patterns
from views.authstatus import authstatus_detail
from views.apidocs import swagger_ui

from api.session import ActiveCount, ActiveList, MacAddress
from api.troubleshooting import AuthStatus, FailureReason

from flask_restful_swagger import swagger

app = Flask(__name__)
# api = Api(app)
api = swagger.docs(Api(app), apiVersion='0.1')

@app.route('/')
def index():
    return render_template('index.html')

# session endpoints
api.add_resource(ActiveList, '/api/session')
api.add_resource(ActiveCount, '/api/session-count')
api.add_resource(MacAddress, '/api/session/<string:mac_address>')

# troubleshooting endpoints
api.add_resource(AuthStatus, '/api/authstatus',
                             '/api/authstatus/<string:mac_address>',
                             '/api/authstatus/<string:mac_address>/<string:duration>',
                             '/api/authstatus/<string:mac_address>/<string:duration>/<string:num_records>',
                             '/api/authstatus/<string:mac_address>/<string:duration>/<string:num_records>/<string:verbosity>')
api.add_resource(FailureReason, '/api/failurereason')



# web views
app.add_url_rule('/session', endpoint='session-list', view_func=session_list)
app.add_url_rule('/patterns', endpoint='patterns', view_func=patterns)
app.add_url_rule('/authstatus-test', endpoint='authstatus-detail', view_func=authstatus_detail)
app.add_url_rule('/apidocs', endpoint='api-docs', view_func=swagger_ui)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
