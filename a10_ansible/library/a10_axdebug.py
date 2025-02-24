#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_axdebug
description:
    - Packet Trace Options
short_description: Configures A10 axdebug
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
        - present
        - absent
        required: True
    a10_host:
        description:
        - Host for AXAPI authentication
        required: True
    a10_username:
        description:
        - Username for AXAPI authentication
        required: True
    a10_password:
        description:
        - Password for AXAPI authentication
        required: True
    a10_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_protocol:
        description:
        - Protocol for AXAPI authentication
        required: True
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    count:
        description:
        - "Maximum packets to capture. Default is 3000. (Maximum packets to capture. For umlimited, specify 0)"
        required: False
    save_config:
        description:
        - "Save AXDebug config file to target filename"
        required: False
    timeout:
        description:
        - "Maximum number of minutes for a capture. Default is 5 minutes. For unlimited, specify 0"
        required: False
    sess_filter_dis:
        description:
        - "Disable session based filter"
        required: False
    outgoing_list:
        description:
        - "Field outgoing_list"
        required: False
        suboptions:
            outgoing:
                description:
                - "Outgoing interface (For all ports, don't specify port number.)"
            out_port_num:
                description:
                - "Port Numbers separated by commas(,) and hyphens(-) without spaces. ex= 4,5,10-30, or separated by spaces and double-quoted(')"
    maxfile:
        description:
        - "Maximum number of debug packet files. Default is 100"
        required: False
    capture:
        description:
        - "Field capture"
        required: False
        suboptions:
            current_slot:
                description:
                - "Only for current-slot of chassis"
            outgoing:
                description:
                - "Outgoing interface"
            non_display:
                description:
                - "Do not print to screen"
            incoming:
                description:
                - "Incoming interface"
            port_num:
                description:
                - "Port Numbers separated by commas(,) and hyphens(-) without spaces (ex= 4,5,10-30), or separated by spaces and double-quoted(')"
            brief:
                description:
                - "Print basic packet information"
            detail:
                description:
                - "Include packet payload"
            save:
                description:
                - "Save packets into file (Specify filename to save packets)"
            max_packets:
                description:
                - "Maximum packets to capture for each data cpu."
    length:
        description:
        - "Packet length to capture, enable jumbo to capture more than 1518 bytes"
        required: False
    exit:
        description:
        - "Exit from axdebug mode"
        required: False
    delete_file_list:
        description:
        - "Field delete_file_list"
        required: False
        suboptions:
            delete_config:
                description:
                - "Delete AXDebug config file (Specify target filename to change)"
            delete_capture:
                description:
                - "Delete a capture file (Specify target filename to change)"
            delete:
                description:
                - "Delete AXDebug capture / config file"
    filter_config:
        description:
        - "Field filter_config"
        required: False
        suboptions:
            arp:
                description:
                - "ARP"
            ip:
                description:
                - "IP"
            offset:
                description:
                - "byte offset"
            number:
                description:
                - "Specify filter id"
            tcp:
                description:
                - "Field tcp"
            l3_proto:
                description:
                - "Layer 3 protocol"
            ipv4_address:
                description:
                - "ip address"
            port:
                description:
                - "port number"
            port_num_min:
                description:
                - "min port number"
            oper_range:
                description:
                - "'gt'= greater than; 'gte'= greater than or equal to; 'se'= smaller than or equal to; 'st'= smaller than; 'eq'= equal to; "
            ipv6_adddress:
                description:
                - "ipv6 address"
            WORD:
                description:
                - "WORD to compare"
            comp_hex:
                description:
                - "value to compare"
            proto:
                description:
                - "ip protocol number"
            dst:
                description:
                - "Destination"
            hex:
                description:
                - "Define hex value"
            integer_comp:
                description:
                - "value to compare"
            port_num_max:
                description:
                - "max port number"
            exit:
                description:
                - "Exit from axdebug mode"
            ipv6:
                description:
                - "IPV6"
            length:
                description:
                - "byte length"
            udp:
                description:
                - "Field udp"
            neighbor:
                description:
                - "IPv6 Neighbor/Router"
            port_num:
                description:
                - "Port number"
            max_hex:
                description:
                - "max value"
            mac:
                description:
                - "mac address"
            min_hex:
                description:
                - "min value"
            WORD1:
                description:
                - "WORD min value"
            WORD2:
                description:
                - "WORD max value"
            integer_max:
                description:
                - "max value"
            integer:
                description:
                - "Define decimal value"
            icmp:
                description:
                - "Field icmp"
            src:
                description:
                - "Source"
            mac_addr:
                description:
                - "mac address"
            ipv4_netmask:
                description:
                - "IP subnet mask"
            icmpv6:
                description:
                - "Field icmpv6"
            range:
                description:
                - "select a range"
            integer_min:
                description:
                - "min value"
            prot_num:
                description:
                - "protocol number"
    incoming_list:
        description:
        - "Field incoming_list"
        required: False
        suboptions:
            incoming:
                description:
                - "Incoming interface. (For all ports, don't specify port number.)"
            inc_port_num:
                description:
                - "Port Numbers separated by commas(,) and hyphens(-) without spaces. ex= 4,5,10-30, or separated by spaces and double-quoted(')"
    apply_config:
        description:
        - "Apply AXDebug config file"
        required: False


"""

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["apply_config","capture","count","delete_file_list","exit","filter_config","incoming_list","length","maxfile","outgoing_list","save_config","sess_filter_dis","timeout",]

# our imports go at the top so we fail fast.
try:
    from a10_ansible import errors as a10_ex
    from a10_ansible.axapi_http import client_factory, session_factory
    from a10_ansible.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        a10_host=dict(type='str', required=True),
        a10_username=dict(type='str', required=True),
        a10_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=["present", "absent", "noop"]),
        a10_port=dict(type='int', required=True),
        a10_protocol=dict(type='str', choices=["http", "https"]),
        a10_partition=dict(type='dict', name=dict(type='str',), shared=dict(type='str',), required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        count=dict(type='int',),
        save_config=dict(type='str',),
        timeout=dict(type='int',),
        sess_filter_dis=dict(type='bool',),
        outgoing_list=dict(type='dict',outgoing=dict(type='bool',),out_port_num=dict(type='str',)),
        maxfile=dict(type='int',),
        capture=dict(type='dict',current_slot=dict(type='bool',),outgoing=dict(type='bool',),non_display=dict(type='bool',),incoming=dict(type='bool',),port_num=dict(type='str',),brief=dict(type='bool',),detail=dict(type='bool',),save=dict(type='str',),max_packets=dict(type='int',)),
        length=dict(type='int',),
        exit=dict(type='bool',),
        delete_file_list=dict(type='dict',delete_config=dict(type='str',),delete_capture=dict(type='str',),delete=dict(type='bool',)),
        filter_config=dict(type='dict',arp=dict(type='bool',),ip=dict(type='bool',),offset=dict(type='int',),number=dict(type='int',),tcp=dict(type='bool',),l3_proto=dict(type='bool',),ipv4_address=dict(type='str',),port=dict(type='bool',),port_num_min=dict(type='int',),oper_range=dict(type='str',choices=['gt','gte','se','st','eq']),ipv6_adddress=dict(type='str',),WORD=dict(type='str',),comp_hex=dict(type='str',),proto=dict(type='bool',),dst=dict(type='bool',),hex=dict(type='bool',),integer_comp=dict(type='int',),port_num_max=dict(type='int',),exit=dict(type='bool',),ipv6=dict(type='bool',),length=dict(type='int',),udp=dict(type='bool',),neighbor=dict(type='bool',),port_num=dict(type='int',),max_hex=dict(type='str',),mac=dict(type='bool',),min_hex=dict(type='str',),WORD1=dict(type='str',),WORD2=dict(type='str',),integer_max=dict(type='int',),integer=dict(type='bool',),icmp=dict(type='bool',),src=dict(type='bool',),mac_addr=dict(type='str',),ipv4_netmask=dict(type='str',),icmpv6=dict(type='bool',),range=dict(type='bool',),integer_min=dict(type='int',),prot_num=dict(type='int',)),
        incoming_list=dict(type='dict',incoming=dict(type='bool',),inc_port_num=dict(type='str',)),
        apply_config=dict(type='str',)
    ))
   

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/axdebug"

    f_dict = {}

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/axdebug"

    f_dict = {}

    return url_base.format(**f_dict)

def oper_url(module):
    """Return the URL for operational data of an existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/oper"

def stats_url(module):
    """Return the URL for statistical data of and existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/stats"

def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]

def build_envelope(title, data):
    return {
        title: data
    }

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if x in params and params.get(x) is not None])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def get(module):
    return module.client.get(existing_url(module))

def get_list(module):
    return module.client.get(list_url(module))

def get_oper(module):
    return module.client.get(oper_url(module))

def get_stats(module):
    return module.client.get(stats_url(module))

def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None

def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["axdebug"].items():
            if v.lower() == "true":
                v = 1
            elif v.lower() == "false":
                v = 0
            if existing_config["axdebug"][k] != v:
                if result["changed"] != True:
                    result["changed"] = True
                existing_config["axdebug"][k] = v
        result.update(**existing_config)
    else:
        result.update(**payload)
    return result

def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.Exists:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result, existing_config):
    payload = build_json("axdebug", module)
    if module.check_mode:
        return report_changes(module, result, existing_config, payload)
    elif not existing_config:
        return create(module, result, payload)
    else:
        return update(module, result, existing_config, payload)

def absent(module, result):
    if module.check_mode:
        result["changed"] = True
        return result
    else:
        return delete(module, result)

def replace(module, result, existing_config):
    payload = build_json("axdebug", module)
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message="",
        result={}
    )

    state = module.params["state"]
    a10_host = module.params["a10_host"]
    a10_username = module.params["a10_username"]
    a10_password = module.params["a10_password"]
    a10_port = module.params["a10_port"] 
    a10_protocol = module.params["a10_protocol"]
    a10_partition = module.params["a10_partition"]

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)
    
    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)
    if a10_partition:
        module.client.activate_partition(a10_partition)

    existing_config = exists(module)

    if state == 'present':
        result = present(module, result, existing_config)
        module.client.session.close()
    elif state == 'absent':
        result = absent(module, result)
        module.client.session.close()
    elif state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
        elif module.params.get("get_type") == "oper":
            result["result"] = get_oper(module)
        elif module.params.get("get_type") == "stats":
            result["result"] = get_stats(module)
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()