
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
