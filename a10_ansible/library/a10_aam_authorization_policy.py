#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_aam_authorization_policy
description:
    - Authorization-policy configuration
short_description: Configures A10 aam.authorization.policy
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
    jwt_authorization:
        description:
        - "Specify JWT authorization template (Specify JWT authorization template name)"
        required: False
    name:
        description:
        - "Specify authorization policy name"
        required: True
    user_tag:
        description:
        - "Customized tag"
        required: False
    server:
        description:
        - "Specify a LDAP or RADIUS server for authorization (Specify a LDAP or RADIUS server name)"
        required: False
    jwt_claim_map_list:
        description:
        - "Field jwt_claim_map_list"
        required: False
        suboptions:
            claim:
                description:
                - "Specify JWT claim name to map to."
            bool_val:
                description:
                - "'true'= True; 'false'= False; "
            uuid:
                description:
                - "uuid of the object"
            string_type:
                description:
                - "Claim type is string"
            str_val:
                description:
                - "Specify JWT claim value."
            num_val:
                description:
                - "Specify JWT claim value."
            attr_num:
                description:
                - "Spcify attribute ID for claim mapping"
            number_type:
                description:
                - "Claim type is number"
            boolean_type:
                description:
                - "Claim type is boolean"
            ntype:
                description:
                - "Specify claim type"
    service_group:
        description:
        - "Specify an authentication service group for authorization (Specify authentication service group name)"
        required: False
    attribute_list:
        description:
        - "Field attribute_list"
        required: False
        suboptions:
            attribute_name:
                description:
                - "Specify attribute name"
            integer_type:
                description:
                - "Attribute type is integer"
            custom_attr_type:
                description:
                - "Specify attribute type"
            uuid:
                description:
                - "uuid of the object"
            string_type:
                description:
                - "Attribute type is string"
            attr_str_val:
                description:
                - "Set attribute value"
            attr_ipv4:
                description:
                - "IPv4 address"
            attr_type:
                description:
                - "Specify attribute type"
            attr_num:
                description:
                - "Set attribute ID for authorization policy"
            a10_dynamic_defined:
                description:
                - "The value of this attribute will depend on AX configuration instead of user configuration"
            attr_int:
                description:
                - "'equal'= Operation type is equal; 'not-equal'= Operation type is not equal; 'less-than'= Operation type is less-than; 'more-than'= Operation type is more-than; 'less-than-equal-to'= Operation type is less-than-equal-to; 'more-than-equal-to'= Operation type is more-thatn-equal-to; "
            ip_type:
                description:
                - "IP address is transformed into network byte order"
            attr_ip:
                description:
                - "'equal'= Operation type is equal; 'not-equal'= Operation type is not-equal; "
            A10_AX_AUTH_URI:
                description:
                - "Custom-defined attribute"
            attr_str:
                description:
                - "'match'= Operation type is match; 'sub-string'= Operation type is sub-string; "
            any:
                description:
                - "Matched when attribute is present (with any value)."
            custom_attr_str:
                description:
                - "'match'= Operation type is match; 'sub-string'= Operation type is sub-string; "
            attr_int_val:
                description:
                - "Set attribute value"
    extended_filter:
        description:
        - "Extended search filter. EX= Check whether user belongs to a nested group. (memberOf=1.2.840.113556.1.4.1941==$GROUP-DN)"
        required: False
    attribute_rule:
        description:
        - "Define attribute rule for authorization policy"
        required: False
    forward_policy_authorize_only:
        description:
        - "This policy only provides server info for forward policy feature"
        required: False
    uuid:
        description:
        - "uuid of the object"
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
AVAILABLE_PROPERTIES = ["attribute_list","attribute_rule","extended_filter","forward_policy_authorize_only","jwt_authorization","jwt_claim_map_list","name","server","service_group","user_tag","uuid",]

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
        jwt_authorization=dict(type='str',),
        name=dict(type='str',required=True,),
        user_tag=dict(type='str',),
        server=dict(type='str',),
        jwt_claim_map_list=dict(type='list',claim=dict(type='str',),bool_val=dict(type='str',choices=['true','false']),uuid=dict(type='str',),string_type=dict(type='bool',),str_val=dict(type='str',),num_val=dict(type='int',),attr_num=dict(type='int',required=True,),number_type=dict(type='bool',),boolean_type=dict(type='bool',),ntype=dict(type='bool',)),
        service_group=dict(type='str',),
        attribute_list=dict(type='list',attribute_name=dict(type='str',),integer_type=dict(type='bool',),custom_attr_type=dict(type='bool',),uuid=dict(type='str',),string_type=dict(type='bool',),attr_str_val=dict(type='str',),attr_ipv4=dict(type='str',),attr_type=dict(type='bool',),attr_num=dict(type='int',required=True,),a10_dynamic_defined=dict(type='bool',),attr_int=dict(type='str',choices=['equal','not-equal','less-than','more-than','less-than-equal-to','more-than-equal-to']),ip_type=dict(type='bool',),attr_ip=dict(type='str',choices=['equal','not-equal']),A10_AX_AUTH_URI=dict(type='bool',),attr_str=dict(type='str',choices=['match','sub-string']),any=dict(type='bool',),custom_attr_str=dict(type='str',choices=['match','sub-string']),attr_int_val=dict(type='int',)),
        extended_filter=dict(type='str',),
        attribute_rule=dict(type='str',),
        forward_policy_authorize_only=dict(type='bool',),
        uuid=dict(type='str',)
    ))
   

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authorization/policy/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authorization/policy/{name}"

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
        for k, v in payload["policy"].items():
            if v.lower() == "true":
                v = 1
            elif v.lower() == "false":
                v = 0
            if existing_config["policy"][k] != v:
                if result["changed"] != True:
                    result["changed"] = True
                existing_config["policy"][k] = v
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
    payload = build_json("policy", module)
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
    payload = build_json("policy", module)
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