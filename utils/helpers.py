from collections import OrderedDict
step_map = {
    11001: "Initializing",
    11017: "RADIUS created a new session",
    11117: "Generated a new session ID",
    11027: "Detected Host Lookup UseCase (Service-Type = Call Check (10))",
    15049: "Evaluating Policy Group",
    15008: "Evaluating Service Selection Policy",
    15048:"Queried PIP - Normalised Radius.RadiusFlowType",
    15048:"Queried PIP - DEVICE.Device Type",
    15004:"Matched rule - MAB",
    15041:"Evaluating Identity Policy",
    15006:"Matched Default Rule",
    15013: "Selected Identity Source - Internal Endpoints",
    24209: "Looking up Endpoint in Internal Endpoints IDStore - 00:00:3A:00:00:00",
    24217: "The host is not found in the internal endpoints identity store",
    22056: "Subject not found in the applicable identity store(s)",
    22058: "The advanced option that is configured for an unknown user is used",
    22060: "The 'Continue' advanced option is configured in case of a failed authentication request",
    15036: "Evaluating Authorization Policy",
    15048: "Queried PIP - Session.ANCPolicy",
    15048: "Queried PIP - Session.PostureStatus",
    15004: "Matched rule - CPP_REDIRECT",
    15016: "Selected Authorization Profile - Posture_Redirect",
    11002: "Returned RADIUS Access-Accept",

}

def fixup_steps(steps):
    """
    returns list of (step, description) for a comma seperated string containing
    step ids
    e.g 11001,11017,11117,11027,15049,15008,15048
    returns [(1101, "Initializing"), .... ]
    """
    step_ids = steps.split(',')
    ret = list()
    for step in step_ids:
        step = int(step)
        desc = step_map.get(step, "unknown step")
        ret.append((step, desc))
    return ret


data = OrderedDict([(u'passed', OrderedDict([(u'@xsi:type', u'xs:boolean'), (u'@xmlns:xs', u'http://www.w3.org/2001/XMLSchema'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), ('#text', u'true')])), (u'failed', OrderedDict([(u'@xsi:type', u'xs:boolean'), (u'@xmlns:xs', u'http://www.w3.org/2001/XMLSchema'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), ('#text', u'false')])), (u'user_name', u'00:00:AA:20:97:BE'), (u'nas_ip_address', u'198.18.134.139'), (u'nas_port_type', u'Ethernet'), (u'calling_station_id', u'00:00:AA:20:97:BE'), (u'identity_group', u'Profiled'), (u'network_device_name', u'aod-switch'), (u'acs_server', u'web'), (u'authentication_method', u'mab'), (u'authentication_protocol', u'Lookup'), (u'framed_ip_address', u'10.0.1.126'), (u'acs_timestamp', u'2017-11-24T11:12:02.980Z'), (u'execution_steps', u'11001,11017,11117,11027,15049,15008,15048,15004,15041,15006,15013,24209,24211,22037,15036,15048,15004,15016,11022,11002'), (u'response', u'{UserName=00:00:AA:20:97:BE; State=ReauthSession:c612851bTxQLrYTTdtmQyjcqJ1ClUr2rQYBA8SjoytlBafk/HRI; Class=CACS:c612851bTxQLrYTTdtmQyjcqJ1ClUr2rQYBA8SjoytlBafk/HRI:web/300739116/41757; Session-Timeout=600; Termination-Action=RADIUS-Request; cisco-av-pair=url-redirect-acl=ACL_WEBAUTH_REDIRECT; cisco-av-pair=url-redirect=https://web.ise-en-001.dc-01.com:8443/portal/gateway?sessionId=c612851bTxQLrYTTdtmQyjcqJ1ClUr2rQYBA8SjoytlBafk/HRI&portal=a692c530-2230-11e6-99ab-005056bf55e0&action=cwa&token=ba44bb95af1f4335bcdf9393fec8dfac; cisco-av-pair=ACS:CiscoSecure-Defined-ACL=#ACSACL#-IP-ACL_WEBAUTH_REDIRECT-57e5bcbd; cisco-av-pair=profile-name=Xerox-Device; LicenseTypes=1; }'), (u'nas_port_id', u'GigabitEthernet2/42'), (u'selected_azn_profiles', u'Cisco_WebAuth'), (u'service_type', u'Call Check'), (u'message_code', u'5200'), (u'id', u'1511364570637287'), (u'acsview_timestamp', u'2017-11-24T11:12:02.981Z'), (u'identity_store', u'Internal Endpoints'), (u'response_time', u'20'), (u'location', u'All Locations#dCloud'), (u'device_type', u'All Device Types#Switches'), (u'other_attributes', u':!:ConfigVersionId=66:!:DestinationPort=1812:!:Protocol=Radius:!:NAS-Port=4928:!:OriginalUserName=00-00-AA-20-97-BE:!:NetworkDeviceProfileName=Cisco:!:NetworkDeviceProfileId=403ea8fc-7a27-41c3-80bb-27964031a08d:!:IsThirdPartyDeviceFlow=false:!:RadiusFlowType=WiredMAB:!:SSID=50-06-04-84-6D-10:!:AcsSessionID=web/300739116/41757:!:UseCase=Host Lookup:!:SelectedAuthenticationIdentityStores=Internal Endpoints:!:AuthenticationStatus=AuthenticationPassed:!:IdentityPolicyMatchedRule=Default876a2385-87c7-446d-9d22-754d31e22f01:!:AuthorizationPolicyMatchedRule=Default:!:CPMSessionID=c612851bTxQLrYTTdtmQyjcqJ1ClUr2rQYBA8SjoytlBafk/HRI:!:EndPointMACAddress=00-00-AA-20-97-BE:!:ISEPolicySetName=Default:!:AllowedProtocolMatchedRule=MAB:!:IdentitySelectionMatchedRule=Default:!:DTLSSupport=Unknown:!:HostIdentityGroup=Endpoint Identity Groups:Profiled:!:Model Name=Unknown:!:Software Version=Unknown:!:Network Device Profile=Cisco:!:Location=Location#All Locations#dCloud:!:Device Type=Device Type#All Device Types#Switches:!:LogicalProfile=Printers:!:StepData="6= Normalised Radius.RadiusFlowType","7=MAB","10=Internal Endpoints","15= EndPoints.LogicalProfile","16=Default"=StepData:!:RADIUS Username=00:00:AA:20:97:BE:!:NAS-Identifier=ise-aod-switch:!:Device IP Address=198.18.134.139:!:Called-Station-ID=50:06:04:84:6D:10:!:CiscoAVPair=')])

def expand_other_attributes(data):
    d = data['other_attributes']
    data['requested_attributes'] = dict()
    attrs = d.split(':!:')
    # remove empty elements
    attrs = filter(None, attrs) # fastes
    for i in attrs:
        lst = i.split('=')
        data['requested_attributes'][lst[0]] = lst[1]

    return data
