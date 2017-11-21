# encoding=utf8
from flask_restful import Resource
import requests
from requests.auth import HTTPBasicAuth
from lxml import etree
import xmltodict
import json


headers = {
    'content-type': "application/xml",
    'accept': "application/xml",
    'authorization': "Basic YWRtaW46V3d3cHJ0cDAz",
    'cache-control': "no-cache",
    }

class ActiveCount(Resource):
    """
    Active sessions (ActiveCount)—An active session is one that is authenticated
    onto the network.
    """

    def get(self):

        url = "https://172.26.159.217/admin/API/mnt/Session/ActiveCount"
        response = requests.get(url, headers=headers, auth=HTTPBasicAuth('amdemo1', 'C1sco12345'), verify=False)
        print response.text
        xmlstr = response.content

        d = xmltodict.parse(response.content)
        print d
        return d


class ActiveList(Resource):
    """
    The following simple session list API calls let you quickly gather
    session-related information such as the MAC address, the network access
    device (NAD) IP address, user name, and session ID associated with a current
    active session on a target Cisco Monitoring ISE node in your Cisco ISE deployment
    """
    def get(self):
        url = "https://172.26.159.217/admin/API/mnt/Session/ActiveList"
        response = requests.get(url, headers=headers, verify=False)
        xmlstr = response.content
        d = xmltodict.parse(response.content)
        try:
            return d['activeList']['activeSession']
        except KeyError:
            # no active sessions
            return []

class MacAddress(Resource):
    """
    You can use the MACAddress API call to retrieve a specified MAC address from
    a current, active session. This API call lists a variety of session-related
    information drawn from node database tables.
    """
    def get(self, mac_address):
        """
        returns active session information based on `mac_address`
        """
        url = "https://172.26.159.217/admin/API/mnt/Session/MACAddress/{}".format(mac_address)
        response = requests.get(url, headers=headers, verify=False)
        xmlstr = response.content
        d = xmltodict.parse(response.content)
        try:
            return d['sessionParameters']
        except KeyError:
            return
