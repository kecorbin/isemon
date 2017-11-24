# encoding=utf8
import sys
from flask_restful import Resource, marshal_with
import requests
from lxml import etree
import xmltodict
import json
from models.failurereason import FailureReasonObject, FailureReasonSwaggerModel
from flask_restful_swagger_2 import swagger

if __name__ == '__main__':
    if __package__ is None:
        sys.path.append(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

from services import ise

doc_template = {
    'tags': ['troubleshooting'],
    'description': """
    You can use the AuthStatus API call to check the authentication status of
    sessions on the target node. The query associated with this API call requires
    at least one MAC address to be searched for a match, with a user-configurable
    limit of the most recent records for the specified MAC address returned.

    The AuthStatus API call lets you configure the following search-related parameters:

    Duration—Defines the number of seconds in which an attempt is made to search
    and retrieve the authentication status records associated with the designated
    MAC address. Valid user-configurable values range from 1 to 864000 seconds
    (10 days). If you enter a value of 0 seconds, this specifies a default
    duration of 10 days.
    Records—Defines the number of session records to be searched per MAC address.
    Valid user-configurable values range from 1 to 500 records.
    If you enter 0, this specifies a default setting of 200 records.

    """,
    'responses': {
        '200': {
            'description': 'Success',
            #'schema': SessionParameters,
            'examples': {
                'application/json': {
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
class AuthStatus(Resource):
    """

    """
    docs = doc_template
    docs['parameters'] = [
        {
            'name': 'mac_address',
            'description': """
MAC address to query, e.g A4:B8:05:63:9D:76
            """,
            #'example': 'A4:B8:05:63:9D:76',
            'in': 'path',
            'type': 'string',
            'required': True
        },
        {
            'name': 'duration',
            'description': """
Defines the number of seconds in which an attempt is made to search
and retrieve the authentication status records associated with the designated
MAC address. Valid user-configurable values range from 1 to 864000 seconds
(10 days). If you enter a value of 0 seconds, this specifies a default
duration of 10 days.
            """
            ,
            #'example': 'A4:B8:05:63:9D:76',
            'in': 'path',
            'type': 'string'
        },
        {
            'name': 'num_records',
            'description': """
Defines the number of session records to be searched per MAC address.
Valid user-configurable values range from 1 to 500 records.
If you enter 0, this specifies a default setting of 200 records.
            """
            ,
            #'example': 'A4:B8:05:63:9D:76',
            'in': 'path',
            'type': 'string'
        },
        {
            'name': 'verbosity',
            'description': """
Defines the number of attributes in the authentication status table that are returned from an authentication status search using the AuthStatus API call. Valid values include 0 (the default), All, or user_name+acs_timestamp (see the AuthStatus schema example, AcctStatus API Output Schema).
– If you enter “0”, the basic attributes are returned. These are listed in the restAuthStatus section of the output schema.

– If you enter “All”, a fuller set of attributes are returned. These are listed in the fullRESTAuthStatus section of the output schema.

– If you enter the values listed in the schema for user_name+acs_timestamp, only those attributes are returned. The user_name and acs_timestamp attributes are listed in the restAuthStatus section of the output schema.
            """
            ,
            #'example': 'A4:B8:05:63:9D:76',
            'in': 'path',
            'type': 'string'
        },


    ]

    @swagger.doc(docs)
    def get(self, mac_address=None, duration="432000", num_records="100", verbosity="All"):
        """
        """
        print("Searching history for {} in the last {} seconds.".format(mac_address,
                                                                        duration))


        if mac_address:
            response = ise.get_authstatus(mac_address)
            # d = [d['authStatusOutputList']['authStatusList']['authStatusElements']]
            return response
            # return d

class FailureReason(Resource):
    @swagger.doc({
        'tags': ['troubleshooting'],
        'description': 'Common Failure Reasons',
        'responses': {
            '200': {
                'description': 'everything looks good',
                'schema': FailureReasonSwaggerModel,
                'examples': {
                    'application/json': {
                        'id': '@1001',
                        'code': 'some cause',
                        'cause': "some resolution"
                    }
                }
            }
        }
     })

    def get(self):
        response = ise.get_failure_reasons()
        d = xmltodict.parse(response.content)
        ret = d['failureReasonList']['failureReason']
        objs = [FailureReasonObject.from_dict(r) for r in ret]
        return ret
