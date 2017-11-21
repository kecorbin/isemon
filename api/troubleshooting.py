# encoding=utf8
import sys
from flask_restful import Resource, marshal_with
import requests
from lxml import etree
import xmltodict
import json
from models.failurereason import FailureReasonObject, FailureReasonSwaggerModel
# test data
import sample_data

from flask_restful_swagger_2 import swagger

headers = {
    'content-type': "application/xml",
    'accept': "application/xml",
    'authorization': "Basic YWRtaW46V3d3cHJ0cDAz",
    'cache-control': "no-cache",
    }


class AuthStatus(Resource):
    """
    You can use the AuthStatus API call to check the authentication status of
    sessions on the target node. The query associated with this API call requires
    at least one MAC address to be searched for a match, with a user-configurable
    limit of the most recent records for the specified MAC address returned.
    """

    def get(self, mac_address=None, duration="432000", num_records="100", verbosity="all"):
        """
        The AuthStatus API call lets you configure the following search-related parameters:

        Duration—Defines the number of seconds in which an attempt is made to search
        and retrieve the authentication status records associated with the designated
        MAC address. Valid user-configurable values range from 1 to 864000 seconds
        (10 days). If you enter a value of 0 seconds, this specifies a default
        duration of 10 days.
        Records—Defines the number of session records to be searched per MAC address.
        Valid user-configurable values range from 1 to 500 records.
        If you enter 0, this specifies a default setting of 200 records.
        """
        print("Searching history for {} in the last {} seconds.".format(mac_address,
                                                                        duration))

        # if mac_address:
        #     uri = "/admin/API/mnt/AuthStatus/MACAddress/{}/{}/{}/{}".format(mac_address,
        #                                                                     duration,
        #                                                                     num_records,
        #                                                                     verbosity)
        # else:
        #     uri = '/admin/API/mnt/AuthStatus'
        # url = "https://172.26.159.217" + uri
        #response = requests.get(url, headers=headers, verify=False)
        #d = xmltodict.parse(response.content)
        data = sample_data.authstatuslist
        d = xmltodict.parse(data)
        d = [d['authStatusOutputList']['authStatusList']['authStatusElements']]

        return d

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
        uri = '/admin/API/mnt/FailureReasons'
        url = "https://172.26.159.217" + uri
        response = requests.get(url, headers=headers, verify=False)
        xmlstr = response.content
        d = xmltodict.parse(response.content)
        ret = d['failureReasonList']['failureReason']
        objs = [FailureReasonObject.from_dict(r) for r in ret]
        return ret
