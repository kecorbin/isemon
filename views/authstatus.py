from flask import render_template, url_for
import requests
import xmltodict
# Since this is not a python package we need to do some work to treat it like
# such.
if __name__ == '__main__':
    if __package__ is None:
        sys.path.append(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

from api.sample_data import authstatuslist
from api.models.authstatus import AuthStatusObject
from services.ise import get_authstatus
from utils.helpers import fixup_steps, expand_other_attributes

def authstatus_search():
    return render_template('authstatus-search.html')
def authstatus_history(mac_address):
    data = get_authstatus(mac_address)
    d = data['authStatusOutputList']['authStatusList']['authStatusElements']
    status_list = [expand_other_attributes(i) for i in d]
    # status_list = [AuthStatusObject.from_dict(d) for d in d]
    return render_template('authstatus-history.html', title="Autentication History", status_list=d)
