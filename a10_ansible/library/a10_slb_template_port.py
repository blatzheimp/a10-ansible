#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_slb_template_port
description:
    - Port template
short_description: Configures A10 slb.template.port
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
    health_check_disable:
        description:
        - "Disable configured health check configuration"
        required: False
    stats_data_action:
        description:
        - "'stats-data-enable'= Enable statistical data collection for real server port; 'stats-data-disable'= Disable statistical data collection for real server port; "
        required: False
    resel_on_reset:
        description:
        - "When receiving reset from server, do the server/port reselection (default is 0, don't do reselection)"
        required: False
    dest_nat:
        description:
        - "Destination NAT"
        required: False
    restore_svc_time:
        description:
        - "put the service back to the rotation after time in seconds"
        required: False
    request_rate_limit:
        description:
        - "Request rate limit"
        required: False
    dynamic_member_priority:
        description:
        - "Set dynamic member's priority (Initial priority (default is 16))"
        required: False
    bw_rate_limit:
        description:
        - "Configure bandwidth rate limit on real server port (Bandwidth rate limit in Kbps)"
        required: False
    slow_start:
        description:
        - "Slowly ramp up the connection number after port is up"
        required: False
    decrement:
        description:
        - "Decrease after every round of DNS query (default is 0)"
        required: False
    conn_limit:
        description:
        - "Connection limit"
        required: False
    retry:
        description:
        - "Maximum retry times before reassign this connection to another server/port (default is 2) (The maximum retry number)"
        required: False
    weight:
        description:
        - "Weight (port weight)"
        required: False
    inband_health_check:
        description:
        - "Use inband traffic to detect port's health status"
        required: False
    resume:
        description:
        - "Resume accepting new connection after connection number drops below threshold (Connection resume threshold)"
        required: False
    rate_interval:
        description:
        - "'100ms'= Use 100 ms as sampling interval; 'second'= Use 1 second as sampling interval; "
        required: False
    no_ssl:
        description:
        - "No SSL"
        required: False
    till:
        description:
        - "Slow start ends when slow start connection limit reaches a number (default 4096) (Slow start ends when connection limit reaches this number)"
        required: False
    flap_period:
        description:
        - "take service out of rotation if max-flaps exceeded within time in seconds"
        required: False
    sub_group:
        description:
        - "Divide service group members into different sub groups (Sub group ID (default is 0))"
        required: False
    dampening_flaps:
        description:
        - "service dampening flaps count (max-flaps allowed in flap period)"
        required: False
    bw_rate_limit_no_logging:
        description:
        - "Do not log bandwidth rate limit related state transitions"
        required: False
    down_grace_period:
        description:
        - "Port down grace period (Down grace period in seconds)"
        required: False
    initial_slow_start:
        description:
        - "Initial slow start connection limit (default 128)"
        required: False
    dscp:
        description:
        - "Differentiated Services Code Point (DSCP to Real Server IP Mapping Value)"
        required: False
    request_rate_interval:
        description:
        - "'100ms'= Use 100 ms as sampling interval; 'second'= Use 1 second as sampling interval; "
        required: False
    add:
        description:
        - "Slow start connection limit add by a number every interval (Add by this number every interval)"
        required: False
    every:
        description:
        - "Slow start connection limit increment interval (default 10)"
        required: False
    shared_partition_pool:
        description:
        - "Reference a NAT pool or pool-group from shared partition"
        required: False
    conn_limit_no_logging:
        description:
        - "Do not log connection over limit event"
        required: False
    extended_stats:
        description:
        - "Enable extended statistics on real server port"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    reset:
        description:
        - "Send client reset when connection rate over limit"
        required: False
    del_session_on_server_down:
        description:
        - "Delete session if the server/port goes down (either disabled/hm down)"
        required: False
    conn_rate_limit_no_logging:
        description:
        - "Do not log connection over limit event"
        required: False
    name:
        description:
        - "Port template name"
        required: True
    template_port_pool_shared:
        description:
        - "Source NAT (IP NAT Pool or pool group name)"
        required: False
    bw_rate_limit_duration:
        description:
        - "Duration in seconds the observed rate needs to honor"
        required: False
    bw_rate_limit_resume:
        description:
        - "Resume server selection after bandwidth drops below this threshold (in Kbps) (Bandwidth rate limit resume threshold (in Kbps))"
        required: False
    user_tag:
        description:
        - "Customized tag"
        required: False
    times:
        description:
        - "Slow start connection limit multiply by a number every interval (default 2) (Multiply by this number every interval)"
        required: False
    request_rate_no_logging:
        description:
        - "Do not log connection over limit event"
        required: False
    down_timer:
        description:
        - "The timer to bring the marked down server/port to up (default is 0, never bring up) (The timer to bring up server (in second, default is 0))"
        required: False
    conn_rate_limit:
        description:
        - "Connection rate limit"
        required: False
    source_nat:
        description:
        - "Source NAT (IP NAT Pool or pool group name)"
        required: False
    reassign:
        description:
        - "Maximum reassign times before declear the server/port down (default is 25) (The maximum reassign number)"
        required: False
    health_check:
        description:
        - "Health Check Monitor (Health monitor name)"
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
AVAILABLE_PROPERTIES = ["add","bw_rate_limit","bw_rate_limit_duration","bw_rate_limit_no_logging","bw_rate_limit_resume","conn_limit","conn_limit_no_logging","conn_rate_limit","conn_rate_limit_no_logging","dampening_flaps","decrement","del_session_on_server_down","dest_nat","down_grace_period","down_timer","dscp","dynamic_member_priority","every","extended_stats","flap_period","health_check","health_check_disable","inband_health_check","initial_slow_start","name","no_ssl","rate_interval","reassign","request_rate_interval","request_rate_limit","request_rate_no_logging","resel_on_reset","reset","restore_svc_time","resume","retry","shared_partition_pool","slow_start","source_nat","stats_data_action","sub_group","template_port_pool_shared","till","times","user_tag","uuid","weight",]

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
        health_check_disable=dict(type='bool',),
        stats_data_action=dict(type='str',choices=['stats-data-enable','stats-data-disable']),
        resel_on_reset=dict(type='bool',),
        dest_nat=dict(type='bool',),
        restore_svc_time=dict(type='int',),
        request_rate_limit=dict(type='int',),
        dynamic_member_priority=dict(type='int',),
        bw_rate_limit=dict(type='int',),
        slow_start=dict(type='bool',),
        decrement=dict(type='int',),
        conn_limit=dict(type='int',),
        retry=dict(type='int',),
        weight=dict(type='int',),
        inband_health_check=dict(type='bool',),
        resume=dict(type='int',),
        rate_interval=dict(type='str',choices=['100ms','second']),
        no_ssl=dict(type='bool',),
        till=dict(type='int',),
        flap_period=dict(type='int',),
        sub_group=dict(type='int',),
        dampening_flaps=dict(type='int',),
        bw_rate_limit_no_logging=dict(type='bool',),
        down_grace_period=dict(type='int',),
        initial_slow_start=dict(type='int',),
        dscp=dict(type='int',),
        request_rate_interval=dict(type='str',choices=['100ms','second']),
        add=dict(type='int',),
        every=dict(type='int',),
        shared_partition_pool=dict(type='bool',),
        conn_limit_no_logging=dict(type='bool',),
        extended_stats=dict(type='bool',),
        uuid=dict(type='str',),
        reset=dict(type='bool',),
        del_session_on_server_down=dict(type='bool',),
        conn_rate_limit_no_logging=dict(type='bool',),
        name=dict(type='str',required=True,),
        template_port_pool_shared=dict(type='str',),
        bw_rate_limit_duration=dict(type='int',),
        bw_rate_limit_resume=dict(type='int',),
        user_tag=dict(type='str',),
        times=dict(type='int',),
        request_rate_no_logging=dict(type='bool',),
        down_timer=dict(type='int',),
        conn_rate_limit=dict(type='int',),
        source_nat=dict(type='str',),
        reassign=dict(type='int',),
        health_check=dict(type='str',)
    ))
   

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/port/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/port/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

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
        for k, v in payload["port"].items():
            if v.lower() == "true":
                v = 1
            elif v.lower() == "false":
                v = 0
            if existing_config["port"][k] != v:
                if result["changed"] != True:
                    result["changed"] = True
                existing_config["port"][k] = v
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
    payload = build_json("port", module)
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
    payload = build_json("port", module)
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