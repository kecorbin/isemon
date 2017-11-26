from flask_restful_swagger_2 import Schema


class SessionParameters(Schema):
    type = "object"
    properties = {
        "grp_mapping_pol_matched_rule": {
            "type": "string",
            "description": "grp_mapping_pol_matched_rule",
            "example": "anexample"
        },
        "execution_steps": {
            "type": "string",
            "description": "execution_steps",
            "example": "11001,11017,11027,15049,15008,15048,15048,15004"
        },
        "acct_class": {
            "type": "string",
            "description": "acct_class",
            "example": "CACS:c612851bGRS6BmQXaNI/ArFapAMD"
        },
        "acct_authentic": {
            "type": "string",
            "description": "acct_authentic",
            "example": "anexample"
        },
        "acct_input_octets": {
            "type": "string",
            "description": "acct_input_octets",
            "example": "anexample"
        },
        "use_case": {
            "type": "string",
            "description": "use_case",
            "example": "anexample"
        },
        "failed": {
            "type": "boolean",
            "description": "failed",
            "example": "false"
        },
        "radius_username": {
            "type": "string",
            "description": "radius_username",
            "example": "anexample"
        },
        "authorization_policy": {
            "type": "string",
            "description": "authorization_policy",
            "example": "anexample"
        },
        "interface_name": {
            "type": "string",
            "description": "interface_name",
            "example": "anexample"
        },
        "calling_station_id": {
            "type": "string",
            "description": "calling_station_id",
            "example": "A4:B8:05:63:9D:76"
        },
        "ad_domain": {
            "type": "string",
            "description": "ad_domain",
            "example": "anexample"
        },
        "termination_action": {
            "type": "string",
            "description": "termination_action",
            "example": "anexample"
        },
        "query_identity_stores": {
            "type": "string",
            "description": "query_identity_stores",
            "example": "anexample"
        },
        "cisco_ssg_attributes": {
            "type": "string",
            "description": "cisco_ssg_attributes",
            "example": "anexample"
        },
        "acct_input_packets": {
            "type": "long",
            "description": "acct_input_packets",
            "example": "anexample"
        },
        "security_group": {
            "type": "string",
            "description": "security_group",
            "example": "anexample"
        },
        "nas_identifier": {
            "type": "string",
            "description": "nas_identifier",
            "example": "anexample"
        },
        "audit_session_id": {
            "type": "string",
            "description": "audit_session_id",
            "example": "anexample"
        },
        "authentication_method": {
            "type": "string",
            "description": "authentication_method",
            "example": "anexample"
        },
        "nas_port_type": {
            "type": "string",
            "description": "nas_port_type",
            "example": "anexample"
        },
        "acct_interim_interval": {
            "type": "string",
            "description": "acct_interim_interval",
            "example": "anexample"
        },
        "authentication_identity_store": {
            "type": "string",
            "description": "authentication_identity_store",
            "example": "anexample"
        },
        "acct_output_octets": {
            "type": "string",
            "description": "acct_output_octets",
            "example": "anexample"
        },
        "cisco_av_pair": {
            "type": "string",
            "description": "cisco_av_pair",
            "example": "anexample"
        },
        "tunnel_details": {
            "type": "string",
            "description": "tunnel_details",
            "example": "anexample"
        },
        "acct_delay_time": {
            "type": "string",
            "description": "acct_delay_time",
            "example": "anexample"
        },
        "network_device_name": {
            "type": "string",
            "description": "network_device_name",
            "example": "anexample"
        },
        "ext_pol_server_matched_rule": {
            "type": "string",
            "description": "ext_pol_server_matched_rule",
            "example": "anexample"
        },
        "acct_id": {
            "type": "long",
            "description": "acct_id",
            "example": "anexample"
        },
        "azn_exp_pol_matched_rule": {
            "type": "string",
            "description": "azn_exp_pol_matched_rule",
            "example": "anexample"
        },
        "nas_port_id": {
            "type": "string",
            "description": "nas_port_id",
            "example": "anexample"
        },
        "stopped": {
            "type": "anyType",
            "description": "stopped",
            "example": "anexample"
        },
        "other_attributes": {
            "type": "string",
            "description": "other_attributes",
            "example": "anexample"
        },
        "nac_posture_token": {
            "type": "string",
            "description": "nac_posture_token",
            "example": "anexample"
        },
        "acs_session_id": {
            "type": "string",
            "description": "acs_session_id",
            "example": "anexample"
        },
        "acs_server": {
            "type": "string",
            "description": "acs_server",
            "example": "anexample"
        },
        "acs_username": {
            "type": "string",
            "description": "acs_username",
            "example": "anexample"
        },
        "reason": {
            "type": "string",
            "description": "reason",
            "example": "anexample"
        },
        "service_selection_policy": {
            "type": "string",
            "description": "service_selection_policy",
            "example": "anexample"
        },
        "nas_port": {
            "type": "string",
            "description": "nas_port",
            "example": "anexample"
        },
        "cisco_h323_connect_time": {
            "type": "string",
            "description": "cisco_h323_connect_time",
            "example": "anexample"
        },
        "response_time": {
            "type": "long",
            "description": "response_time",
            "example": "anexample"
        },
        "selected_posture_server": {
            "type": "string",
            "description": "selected_posture_server",
            "example": "anexample"
        },
        "auth_acs_timestamp": {
            "type": "string",
            "description": "auth_acs_timestamp",
            "example": "anexample"
        },
        "failure_reason": {
            "type": "string",
            "description": "failure_reason",
            "example": "anexample"
        },
        "acct_terminate_cause": {
            "type": "string",
            "description": "acct_terminate_cause",
            "example": "anexample"
        },
        "identity_store": {
            "type": "string",
            "description": "identity_store",
            "example": "anexample"
        },
        "nad_acsview_timestamp": {
            "type": "string",
            "description": "nad_acsview_timestamp",
            "example": "anexample"
        },
        "eap_tunnel": {
            "type": "string",
            "description": "eap_tunnel",
            "example": "anexample"
        },
        "auth_acsview_timestamp": {
            "type": "string",
            "description": "auth_acsview_timestamp",
            "example": "anexample"
        },
        "nad_failure": {
            "type": "anyType",
            "description": "nad_failure",
            "example": "anexample"
        },
        "authentication_type": {
            "type": "string",
            "description": "authentication_type",
            "example": "anexample"
        },
        "nac_policy_compliance": {
            "type": "string",
            "description": "nac_policy_compliance",
            "example": "anexample"
        },
        "cisco_h323_setup_time": {
            "type": "string",
            "description": "cisco_h323_setup_time",
            "example": "anexample"
        },
        "type": {
            "type": "long",
            "description": "type",
            "example": "anexample"
        },
        "acct_multi_session_id": {
            "type": "string",
            "description": "acct_multi_session_id",
            "example": "anexample"
        },
        "passed": {
            "type": "boolean",
            "description": "passed",
            "example": "true"
        },
        "acct_output_packets": {
            "type": "long",
            "description": "acct_output_packets",
            "example": "anexample"
        },
        "started": {
            "type": "anyType",
            "description": "started",
            "example": "anexample"
        },
        "endpoint_policy": {
            "type": "string",
            "description": "endpoint_policy",
            "example": "anexample"
        },
        "nac_radius_is_user_auth": {
            "type": "string",
            "description": "nac_radius_is_user_auth",
            "example": "anexample"
        },
        "acct_tunnel_connection": {
            "type": "string",
            "description": "acct_tunnel_connection",
            "example": "anexample"
        },
        "selected_query_identity_stores": {
            "type": "string",
            "description": "selected_query_identity_stores",
            "example": "anexample"
        },
        "acct_status_type": {
            "type": "string",
            "description": "acct_status_type",
            "example": "anexample"
        },
        "acct_tunnel_packet_lost": {
            "type": "string",
            "description": "acct_tunnel_packet_lost",
            "example": "anexample"
        },
        "acct_acs_timestamp": {
            "type": "string",
            "description": "acct_acs_timestamp",
            "example": "anexample"
        },
        "nac_username": {
            "type": "string",
            "description": "nac_username",
            "example": "anexample"
        },
        "user_name": {
            "type": "string",
            "description": "user_name",
            "example": "john_doe"
        },
        "cisco_h323_attributes": {
            "type": "string",
            "description": "cisco_h323_attributes",
            "example": "anexample"
        },
        "session_timeout": {
            "type": "string",
            "description": "session_timeout",
            "example": "anexample"
        },
        "authen_protocol": {
            "type": "string",
            "description": "authen_protocol",
            "example": "anexample"
        },
        "framed_protocol": {
            "type": "string",
            "description": "framed_protocol",
            "example": "anexample"
        },
        "selected_azn_profiles": {
            "type": "string",
            "description": "selected_azn_profiles",
            "example": "anexample"
        },
        "destination_ip_address": {
            "type": "string",
            "description": "destination_ip_address",
            "example": "anexample"
        },
        "acct_session_time": {
            "type": "long",
            "description": "acct_session_time",
            "example": "anexample"
        },
        "ckpt_id": {
            "type": "long",
            "description": "ckpt_id",
            "example": "anexample"
        },
        "auth_id": {
            "type": "long",
            "description": "auth_id",
            "example": "anexample"
        },
        "identity_policy_matched_rule": {
            "type": "string",
            "description": "identity_policy_matched_rule",
            "example": "anexample"
        },
        "dacl": {
            "type": "string",
            "description": "dacl",
            "example": "anexample"
        },
        "selected_identity_store": {
            "type": "string",
            "description": "selected_identity_store",
            "example": "anexample"
        },
        "nas_ip_address": {
            "type": "string",
            "description": "nas_ip_address",
            "example": "198.18.134.139"
        },
        "nac_role": {
            "type": "string",
            "description": "nac_role",
            "example": "anexample"
        },
        "cisco_h323_disconnect_time": {
            "type": "string",
            "description": "cisco_h323_disconnect_time",
            "example": "anexample"
        },
        "identity_group": {
            "type": "string",
            "description": "identity_group",
            "example": "anexample"
        },
        "service_type": {
            "type": "string",
            "description": "service_type",
            "example": "anexample"
        },
        "network_device_groups": {
            "type": "string",
            "description": "network_device_groups",
            "example": "anexample"
        },
        "sel_exp_azn_profiles": {
            "type": "string",
            "description": "sel_exp_azn_profiles",
            "example": "anexample"
        },
        "vlan": {
            "type": "string",
            "description": "vlan",
            "example": "anexample"
        },
        "access_service": {
            "type": "string",
            "description": "access_service",
            "example": "anexample"
        },
        "idle_timeout": {
            "type": "string",
            "description": "idle_timeout",
            "example": "anexample"
        },
        "message_code": {
            "type": "string",
            "description": "message_code",
            "example": "anexample"
        },
        "response": {
            "type": "string",
            "description": "response",
            "example": "anexample"
        },
        "acct_acsview_timestamp": {
            "type": "string",
            "description": "acct_acsview_timestamp",
            "example": "anexample"
        },
        "cts_security_group": {
            "type": "string",
            "description": "cts_security_group",
            "example": "anexample"
        },
        "event_timestamp": {
            "type": "string",
            "description": "event_timestamp",
            "example": "anexample"
        },
        "acct_session_id": {
            "type": "string",
            "description": "acct_session_id",
            "example": "anexample"
        },
        "radius_response": {
            "type": "string",
            "description": "radius_response",
            "example": "anexample"
        },
        "framed_ip_address": {
            "type": "string",
            "description": "framed_ip_address",
            "example": "anexample"
        }
    }
