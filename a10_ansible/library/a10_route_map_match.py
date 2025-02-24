#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_route_map_match
description:
    - Match values from routing table
short_description: Configures A10 route.map.match
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
    sequence:
        description:
        - Key to identify parent object
    action:
        description:
        - Key to identify parent object
    route_map_tag:
        description:
        - Key to identify parent object
    extcommunity:
        description:
        - "Field extcommunity"
        required: False
        suboptions:
            extcommunity_l_name:
                description:
                - "Field extcommunity_l_name"
    origin:
        description:
        - "Field origin"
        required: False
        suboptions:
            egp:
                description:
                - "remote EGP"
            incomplete:
                description:
                - "unknown heritage"
            igp:
                description:
                - "local IGP"
    group:
        description:
        - "Field group"
        required: False
        suboptions:
            group_id:
                description:
                - "HA or VRRP-A group id"
            ha_state:
                description:
                - "'active'= HA or VRRP-A in Active State; 'standby'= HA or VRRP-A in Standby State; "
    uuid:
        description:
        - "uuid of the object"
        required: False
    ip:
        description:
        - "Field ip"
        required: False
        suboptions:
            peer:
                description:
                - "Field peer"
            next_hop:
                description:
                - "Field next_hop"
            address:
                description:
                - "Field address"
    metric:
        description:
        - "Field metric"
        required: False
        suboptions:
            value:
                description:
                - "Metric value"
    as_path:
        description:
        - "Field as_path"
        required: False
        suboptions:
            name:
                description:
                - "AS path access-list name"
    community:
        description:
        - "Field community"
        required: False
        suboptions:
            name_cfg:
                description:
                - "Field name_cfg"
    local_preference:
        description:
        - "Field local_preference"
        required: False
        suboptions:
            val:
                description:
                - "Preference value"
    route_type:
        description:
        - "Field route_type"
        required: False
        suboptions:
            external:
                description:
                - "Field external"
    tag:
        description:
        - "Field tag"
        required: False
        suboptions:
            value:
                description:
                - "Tag value"
    ipv6:
        description:
        - "Field ipv6"
        required: False
        suboptions:
            next_hop_1:
                description:
                - "Field next_hop_1"
            peer_1:
                description:
                - "Field peer_1"
            address_1:
                description:
                - "Field address_1"
    interface:
        description:
        - "Field interface"
        required: False
        suboptions:
            tunnel:
                description:
                - "Tunnel interface (Tunnel interface number)"
            ethernet:
                description:
                - "Ethernet interface (Port number)"
            loopback:
                description:
                - "Loopback interface (Port number)"
            ve:
                description:
                - "Virtual ethernet interface (Virtual ethernet interface number)"
            trunk:
                description:
                - "Trunk Interface (Trunk interface number)"
    scaleout:
        description:
        - "Field scaleout"
        required: False
        suboptions:
            cluster_id:
                description:
                - "Scaleout Cluster-id"
            operational_state:
                description:
                - "'up'= Scaleout is up and running; 'down'= Scaleout is down or disabled; "


"""

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["as_path","community","extcommunity","group","interface","ip","ipv6","local_preference","metric","origin","route_type","scaleout","tag","uuid",]

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
        extcommunity=dict(type='dict',extcommunity_l_name=dict(type='dict',exact_match=dict(type='bool',),name=dict(type='str',))),
        origin=dict(type='dict',egp=dict(type='bool',),incomplete=dict(type='bool',),igp=dict(type='bool',)),
        group=dict(type='dict',group_id=dict(type='int',),ha_state=dict(type='str',choices=['active','standby'])),
        uuid=dict(type='str',),
        ip=dict(type='dict',peer=dict(type='dict',acl1=dict(type='int',),acl2=dict(type='int',),name=dict(type='str',)),next_hop=dict(type='dict',acl1=dict(type='int',),acl2=dict(type='int',),name=dict(type='str',),prefix_list_1=dict(type='dict',name=dict(type='str',))),address=dict(type='dict',acl1=dict(type='int',),acl2=dict(type='int',),prefix_list=dict(type='dict',name=dict(type='str',)),name=dict(type='str',))),
        metric=dict(type='dict',value=dict(type='int',)),
        as_path=dict(type='dict',name=dict(type='str',)),
        community=dict(type='dict',name_cfg=dict(type='dict',exact_match=dict(type='bool',),name=dict(type='str',))),
        local_preference=dict(type='dict',val=dict(type='int',)),
        route_type=dict(type='dict',external=dict(type='dict',value=dict(type='str',choices=['type-1','type-2']))),
        tag=dict(type='dict',value=dict(type='int',)),
        ipv6=dict(type='dict',next_hop_1=dict(type='dict',prefix_list_name=dict(type='str',),v6_addr=dict(type='str',),next_hop_acl_name=dict(type='str',)),peer_1=dict(type='dict',acl1=dict(type='int',),acl2=dict(type='int',),name=dict(type='str',)),address_1=dict(type='dict',name=dict(type='str',),prefix_list_2=dict(type='dict',name=dict(type='str',)))),
        interface=dict(type='dict',tunnel=dict(type='str',),ethernet=dict(type='str',),loopback=dict(type='int',),ve=dict(type='int',),trunk=dict(type='int',)),
        scaleout=dict(type='dict',cluster_id=dict(type='int',),operational_state=dict(type='str',choices=['up','down']))
    ))
   
    # Parent keys
    rv.update(dict(
        sequence=dict(type='str', required=True),
        action=dict(type='str', required=True),
        route_map_tag=dict(type='str', required=True),
    ))

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/route-map/{route_map_tag}+{action}+{sequence}/match"

    f_dict = {}
    f_dict["sequence"] = module.params["sequence"]
    f_dict["action"] = module.params["action"]
    f_dict["route_map_tag"] = module.params["route_map_tag"]

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/route-map/{route_map_tag}+{action}+{sequence}/match"

    f_dict = {}
    f_dict["sequence"] = module.params["sequence"]
    f_dict["action"] = module.params["action"]
    f_dict["route_map_tag"] = module.params["route_map_tag"]

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
        for k, v in payload["match"].items():
            if v.lower() == "true":
                v = 1
            elif v.lower() == "false":
                v = 0
            if existing_config["match"][k] != v:
                if result["changed"] != True:
                    result["changed"] = True
                existing_config["match"][k] = v
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
    payload = build_json("match", module)
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
    payload = build_json("match", module)
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