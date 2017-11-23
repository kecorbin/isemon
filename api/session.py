# encoding=utf8
import requests
import xmltodict
import json
from collections import OrderedDict
from flask_restful import Resource
from requests.auth import HTTPBasicAuth
from lxml import etree

from models.authstatus import AuthStatusSwaggerModel
from models.session import SessionParameters
from flask_restful_swagger_2 import swagger

if __name__ == '__main__':
    if __package__ is None:
        sys.path.append(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

from services import ise

doc_template = {
    'tags': ['sessions'],
    'description': """
    You can use the session detail API to quickly search the latest session
    list based on key attributes
    """,
    'responses': {
        '200': {
            'description': 'Success',
            'schema': SessionParameters,
            'examples': {
                'application/json': {
                    "sessionParameters": {
                        "passed": {
                            "@xsi:type": "xs:boolean",
                            "@xmlns:xs": "http://www.w3.org/2001/XMLSchema",
                            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                            "#text": "true"
                        },
                        "failed": {
                            "@xsi:type": "xs:boolean",
                            "@xmlns:xs": "http://www.w3.org/2001/XMLSchema",
                            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                            "#text": "false"
                        },
                        "user_name": "john_doe",
                        "nas_ip_address": "198.18.134.139",
                        "calling_station_id": "A4:B8:05:63:9D:76",
                    }
                }
            }
        },
        '404': {
            'description': "No session information found for the query parameters"
        },
        '500': {
            'description': "Internal Server Error"
        }
    }
}

class ActiveSessionCount(Resource):
    """
    Active sessions (ActiveCount)—An active session is one that is authenticated
    onto the network.
    """

    def get(self):
        response = ise.get_active_count()
        xmlstr = response.content
        d = xmltodict.parse(response.content)
        return d

class AuthenticatedSessionList(Resource):
    """
    You can use the AuthList API call to retrieve a list of all currently active authenticated sessions.
    """
    def get(self):
        response = ise.get_authenticated_list()
        xmlstr = response.content
        d = xmltodict.parse(response.content)
        try:
            return d
        except KeyError:
            # no active sessions
            return []


class ActiveSessionList(Resource):
    """
    You can use the ActiveList API call to list all currently active sessions.
    """
    docs = doc_template
    docs['description'] = "retrieve all active sessions"
    @swagger.doc(docs)
    def get(self):
        response = ise.get_active_list()
        xmlstr = response.content
        d = xmltodict.parse(response.content)
        try:
            return d['activeList']['activeSession']
        except KeyError:
            # no active sessions
            return []

class SessionDetail(Resource):
    pass
    # def _get_json(self, **kwargs):
    #     """
    #     responsible for fetching data from ISE service, and converting to json
    #     """
    #     response = ise.get_session_details_by_attr(**kwargs)
    #     xmlstr = response.content
    #     d = xmltodict.parse(response.content)
    #     if response.ok:
    #         return d
    #     elif response.status_code == 500:
    #         # ISE returns 500 when session data is not found, should be 404
    #         try:
    #             error = d['mnt-rest-result']['internal-error-info']
    #             if "not available" in error:
    #                 return {"status": "No Session information Found"}, 404
    #         except:
    #             return "Server Error", 500


class SessionDetailByMAC(SessionDetail):

    docs = doc_template
    docs['description'] = "Gets session details based on mac address"
    docs['parameters'] = [
        {
            'name': 'mac_address',
            'description': 'MAC address to query, e.g A4:B8:05:63:9D:76',
            #'example': 'A4:B8:05:63:9D:76',
            'in': 'path',
            'type': 'string'
        }
    ]

    @swagger.doc(docs)
    def get(self, mac_address):
        """
        returns active session information based on `mac_address`
        """
        response = ise.get_session_details_by_attr(mac_address=mac_address, fmt='json')
        return response

class SessionDetailByIP(SessionDetail):
    docs = doc_template
    docs['description'] = "Gets session details based on IP address"
    docs['parameters'] = [
        {
            'name': 'ip_address',
            'description': "IP address to query, e.g 192.168.1.1",
            'in': 'path',
            'type': 'string'
        }
    ]

    @swagger.doc(docs)
    def get(self, ip_address):
        """
        returns active session information for `ip_address`
        """
        return ise.get_session_details_by_attr(endpoint_ip_address=ip_address, fmt='json')

class SessionDetailByUser(SessionDetail):
    docs = doc_template
    docs['description'] = "Gets session details for `user_name`"
    docs['parameters'] = [
        {
            'name': 'user_name',
            'description': "Username to query, e.g ehosmer",
            'in': 'path',
            'type': 'string'
        }
    ]

    @swagger.doc(docs)
    def get(self, user_name):
        """
        returns active session information for `user_name`
        """
        return ise.get_session_details_by_attr(user_name=user_name, fmt='json')

class SessionDetailByNAS(SessionDetail):
    docs = doc_template
    docs['description'] = "Gets session details for `nas_ip_address`"
    docs['parameters'] = [
        {
            'name': 'nas_ip_address',
            'description': "NAS IP to query, e.g 1.1.1.1",
            'in': 'path',
            'type': 'string'
        }
    ]

    @swagger.doc(docs)
    def get(self, nas_ip_address):
        """
        returns active session information for `nas_ip_address`
        """
        return ise.get_session_details_by_attr(nas_ip_address=nas_ip_address, fmt='json')
