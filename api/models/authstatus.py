from flask_restful_swagger_2 import Schema

class AuthStatusSwaggerModel(Schema):
      type = "object"
      properties = {
        "user_name": {
          "type": "string",
          "description": "Username",
          "example": "john_doe"
        },
        "nas_ip_address": {
          "type": "string",
          "description": "IP address/hostname for the network access device",
          "example": "10.77.152.209"
        },
        "nas_ipv6_address": {
          "type": "string",
          "description": "IPv6 address/hostname for the network access device",
          "example": "2001:cdba::3257:9652"
        },
        "failure_reason": {
          "type": "string",
          "description": "Reason for session authentication failure"
        },
        "calling_station_id": {
          "type": "string",
          "description": "source ip address",
          "example": "00:0C:29:46:F3:B8"
        },
        "nas_port": {
          "type": "string",
          "description": "network access server port"
        },
        "identity_group": {
          "type": "string",
          "description": "a logical group consisting of related users and hosts",
          "example": "Guest_IDG"
        },
        "network_device_name": {
          "type": "string",
          "description": "name of the network device",
          "example": "switch"
        },
        "acs_server": {
          "type": "string",
          "description": "name of the ISE appliance",
          "example": "ise-server1.company.com"
        },
        "eap_authentication": {
          "type": "string",
          "description": "EAP method used for authentication request"
        },
        "framed_ip_address": {
          "type": "string",
          "description": "address configured for a specific user",
          "example": "11011"
        },
        "framed_ipv6_address": {
          "type": "string",
          "description": "address configured for a specific user",
          "example": "11011"
        },
        "network_device_groups": {
          "type": "string",
          "description": "a logical group consisting of related network devices"
        },
        "access_service": {
          "type": "string",
          "description": "applied access service",
          "example": "11011"
        },
        "acs_timestamp": {
          "type": "string",
          "description": "timestamp that is associated with the Cisco ISE authentication request",
          "example": "2017-11-15T10:50:56.515Z"
        },
        "authentication_method": {
          "type": "string",
          "description": "identifies the method used in authentication",
          "example": "mab"
        },
        "execution_steps": {
          "type": "string",
          "description": "list of message codes for each diagnostic message logged while processing the request",
          "example": "11001,11017,11027,15049,15008,15048,15048,15004,15041,15006,15013,24209,24211,22037,15036,15048,15004,15016,11022,11002"
        },
        "radius_response": {
          "type": "string",
          "description": "type of RADIUS response e.g VLAN or ACL"
        },
        "audit_session_id": {
          "type": "string",
          "description": "id of the authentication session",
          "example": "0A4D98D1000001F26F0C04D9"
        },
        "nas_identifier": {
          "type": "string",
          "description": "a network access server (NAS) associated with a specific resource"
        },
        "nas_port_id": {
          "type": "string",
          "description": "id of the NAS port used",
          "example": "GigabitEthernet1/0/17"
        },
        "nac_policy_compliance": {
          "type": "string",
          "description": "reflects posture statics (compliant or non-complaint)",
          "example": "compliant"
        },
        "selected_azn_profiles": {
          "type": "string",
          "description": "identifies the profile used in authentication",
          "example": "CWA_Redirect"
        },
        "service_type": {
          "type": "string",
          "description": "indicates a framed user",
          "example": "Call Check"
        },
        "eap_tunnel": {
          "type": "string",
          "description": "tunnel or outer method used for EAP authentication"
        },
        "message_code": {
          "type": "string",
          "description": "identifier of the audit message that defines the processed request result",
          "example": "5231"
        },
        "destination_ip_address": {
          "type": "string",
          "description": "identifies the destination ip address"
        }
      }
    

class AuthStatusObject(object):
    """
    an Authentication Status
    """

    def __init__(self, **kwargs):
        self._attributes = kwargs
        self._attributes = self._attributes['authStatusList']['authStatusElements']
        print self._attributes.keys()
    @classmethod
    def from_dict(cls, dikt):
        obj = cls(**dikt)
        return obj

    @property
    def passed(self):
        return self._attributes.get("passed", None)

    @property
    def failed(self):
        return self._attributes.get("failed", None)

    @property
    def user_name(self):
        """
        user Name
        """
        return self._attributes.get("user_name", None)

    @property
    def nas_ip_address(self):
        """
        IP address/hostname for the network access devices
        """
        return self._attributes.get("nas_ip_address", None)

    @property
    def nas_ipv6_address(self):
        """
        IPv6 address/hostname for the network access device
        """
        return self._attributes.get("nas_ipv6_address", None)

    @property
    def failure_reason(self):
        """
        Reason for session authentication failure
        """
        return self._attributes.get("failure_reason", None)

    @property
    def calling_station_id(self):
        """
        Source IP address
        """
        return self._attributes.get("calling_station_id", None)

    @property
    def nas_port(self):
        """
        Network access server port
        """
        return self._attributes.get("nas_port", None)

    @property
    def identity_group(self):
        """
        A logical group consisting of related users and hosts
        """
        return self._attributes.get("identity_group", None)

    @property
    def network_device_name(self):
        """
        Name of the network device
        """
        return self._attributes.get("network_device_name", None)

    @property
    def acs_server(self):
        """
        Name of the Cisco ISE appliance
        """
        return self._attributes.get("acs_server", None)

    @property
    def eap_authentication(self):
        """
        Extensible Authentication Protocol (EAP) method used for authentication request
        """
        return self._attributes.get("eap_authentication", None)

    @property
    def framed_ip_address(self):
        """
        Address configured for a specific user
        """
        return self._attributes.get("framed_ip_address", None)

    @property
    def framed_ipv6_address(self):
        """
        Address configured for a specific user
        """
        return self._attributes.get("framed_ipv6_address", None)

    @property
    def network_device_groups(self):
        """
        A logical group consisting of related network devices
        """
        return self._attributes.get("network_device_groups", None)

    @property
    def access_service(self):
        """
        Applied access service
        """
        return self._attributes.get("access_service", None)

    @property
    def acs_timestamp(self):
        """
        Time stamp that is associated with the Cisco ISE authentication request
        """
        return self._attributes.get("acs_timestamp", None)

    @property
    def authentication_method(self):
        """
        Identifies the method used in authentication
        """
        return self._attributes.get("authentication_method", None)

    @property
    def execution_steps(self):
        """
        List of message codes for each diagnostic message logged while processing the request
        """
        return self._attributes.get("execution_steps", None)

    @property
    def radius_response(self):
        """
        Type of RADIUS response (for example, VLAN or ACL)
        """
        return self._attributes.get("radius_response", None)

    @property
    def audit_session_id(self):
        """
        ID of the authentication session
        """
        return self._attributes.get("audit_session_id", None)

    @property
    def nas_identifier(self):
        """
        A network access server (NAS) associated with a specific resource
        """
        return self._attributes.get("nas_identifier", None)

    @property
    def nas_port_id(self):
        """
        ID of the NAS port used
        """
        return self._attributes.get("nas_port_id", None)

    @property
    def nac_policy_compliance(self):
        """
        Reflects Posture status (compliant or non-compliant)
        """
        return self._attributes.get("nac_policy_compliance", None)

    @property
    def selected_azn_profiles(self):
        """
        Identifies the profile used in authorization
        """
        return self._attributes.get("selected_azn_profiles", None)

    @property
    def service_type(self):
        """
        Indicates a framed user
        """
        return self._attributes.get("service_type", None)

    @property
    def eap_tunnel(self):
        """
        Tunnel or outer method used for EAP authentication
        """
        return self._attributes.get("eap_tunnel", None)

    @property
    def message_code(self):
        """
        Identifier of the audit message that defines the processed request result
        """
        return self._attributes.get("message_code", None)

    @property
    def destination_ip_address(self):
        """
        Identifies the destination IP address
        """
        return self._attributes.get("destination_ip_address", None)
