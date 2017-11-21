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

def authstatus_detail():
    # TODO remove sample data
    data = authstatuslist
    data = xmltodict.parse(data)
    d = [data['authStatusOutputList']]
    status_list = [AuthStatusObject.from_dict(d) for d in d]

    return render_template('authstatus-detail.html', status_list=status_list)
