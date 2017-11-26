from flask import render_template

if __name__ == '__main__':
    if __package__ is None:
        sys.path.append(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

from isemon.services import ise
from isemon.utils.helpers import fixup_steps, expand_other_attributes
def session_list():
    return render_template('session-list.html', title="Active Sessions")

def session_detail(mac_address):
    session = ise.get_session_details_by_attr(mac_address=mac_address, fmt='json')
    session = session['sessionParameters']
    steps = fixup_steps(session['execution_steps'])
    return render_template('session-detail.html',
                           title="Authentication Session Detail Report",
                           session=session, steps=steps)
