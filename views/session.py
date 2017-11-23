from flask import render_template

if __name__ == '__main__':
    if __package__ is None:
        sys.path.append(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

from services import ise

def session_list():
    return render_template('session-list.html')

def session_detail(mac_address):
    session = ise.get_session_details_by_attr(mac_address=mac_address, fmt='json')
    session = session['sessionParameters']
    
    return render_template('session-detail.html', session=session)
