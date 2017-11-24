import os
import requests
from requests.auth import HTTPBasicAuth
import urllib3
import xmltodict

urllib3.disable_warnings()


ISE_SERVER = os.getenv("ISE_SERVER")
BASE_URL = "https://{}".format(ISE_SERVER)
USERNAME = os.getenv("ISE_USERNAME")
PASSWORD = os.getenv("ISE_PASSWORD")

if not all([ISE_SERVER, BASE_URL, USERNAME, PASSWORD]):
    raise KeyError("Missing one of ISE_SERVER, ISE_USERNAME, or ISE_PASSWORD")

def get_from_ise(uri):
    headers = {
        'content-type': "application/xml",
        'accept': "application/xml",
        }
    url = BASE_URL + uri
    print("Fetching {} from ISE: ".format(url)),
    response = requests.get(url,
                            headers=headers,
                            auth=HTTPBasicAuth(USERNAME, PASSWORD),
                            verify=False)
    return response


def get_json(url):
    """
    responsible for fetching data from ISE service, and converting to json
    """
    response = get_from_ise(url)
    xmlstr = response.content
    print response.content
    d = xmltodict.parse(response.content)
    if response.ok:
        return d
    elif response.status_code == 500:
        # ISE returns 500 when session data is not found, should be 404
        try:
            error = d['mnt-rest-result']['internal-error-info']
            if "not available" in error:
                return {"status": "No Session information Found"}, 404
        except:
            return "Server Error", 500


def get_active_count():
    uri = "/admin/API/mnt/Session/ActiveCount"
    resp = get_from_ise(uri)
    return resp

def get_active_list():
    uri = "/admin/API/mnt/Session/ActiveList"
    resp = get_from_ise(uri)
    return resp

def get_authenticated_list():
    uri = "/admin/API/mnt/Session/AuthList"
    resp = get_from_ise(uri)
    return resp

def get_session_details_by_attr(mac_address=None,
                                user_name=None,
                                nas_ip_address=None,
                                endpoint_ip_address=None,
                                audit_session_id=None,
                                fmt=None):
    if mac_address:
        attr_type, attr_name = ("MACAddress", mac_address)
    elif user_name:
        attr_type, attr_name = ("UserName", user_name)
    elif nas_ip_address:
        attr_type, attr_name = ("IPAddress", nas_ip_address)
    elif endpoint_ip_address:
        attr_type, attr_name = ("EndPointIPAddress", endpoint_ip_address)
    elif audit_session_id:
        raise NotImplementedError

    uri = "/admin/API/mnt/Session/{}".format(attr_type)
    uri = uri + "/{}".format(attr_name)


    if fmt == 'json':
        resp = get_json(uri)
    else:
        resp = get_from_ise(uri)

    return resp

def get_authstatus(mac_address,
                   duration="432000",
                   num_records="100",
                   verbosity="All"):

    uri = "/admin/API/mnt/AuthStatus/MACAddress"
    uri = uri + "/{}/{}/{}/{}".format(mac_address,
                                       duration,
                                       num_records,
                                       verbosity)
    resp = get_json(uri)
    return resp

def get_failure_reasons():
    uri = '/admin/API/mnt/FailureReasons'
    resp = get_from_ise(url)
    return resp

def get_failure_by_id(id):
    resp = get_failure_reasons()
    xmlstr = resp.content
    d = xmltodict.parse(resp.content)
    reasons = d['failureReasonList']['failureReason']
    reason = [r for r in reasons if r['@id'] == id][0]
    return reason
