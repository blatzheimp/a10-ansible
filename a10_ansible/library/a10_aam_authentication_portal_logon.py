#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_aam_authentication_portal_logon
description:
    - Logon page configuration
short_description: Configures A10 aam.authentication.portal.logon
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
    portal_name:
        description:
        - Key to identify parent object
    action_url:
        description:
        - "Specify form action URL in default logon page (Default= /logon.fo)"
        required: False
    submit_text:
        description:
        - "Specify submit button text in default logon page (Default= Log In)"
        required: False
    passcode_cfg:
        description:
        - "Field passcode_cfg"
        required: False
        suboptions:
            passcode_font_custom:
                description:
                - "Specify custom font"
            passcode_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana; "
            passcode_color:
                description:
                - "Specify font color (Default= black)"
            passcode_text:
                description:
                - "Specify passcode text (Default= Passcode)"
            passcode_color_value:
                description:
                - "Specify 6-digit HEX color value"
            passcode_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow; "
            passcode_font:
                description:
                - "Sepcify font (Default= Arial)"
            passcode:
                description:
                - "Configure passcode text in default logon page"
            passcode_size:
                description:
                - "Specify font size (Default= 3)"
    username_cfg:
        description:
        - "Field username_cfg"
        required: False
        suboptions:
            username:
                description:
                - "Configure username text in default logon page"
            user_font:
                description:
                - "Sepcify font (Default= Arial)"
            user_text:
                description:
                - "Specify username text (Default= User Name)"
            user_size:
                description:
                - "Specify font size (Default= 3)"
            user_color_value:
                description:
                - "Specify 6-digit HEX color value"
            user_font_custom:
                description:
                - "Specify custom font"
            user_color:
                description:
                - "Specify font color (Default= black)"
            user_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana; "
            user_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow; "
    username_var:
        description:
        - "Specify username variable name in default logon page (Default= user)"
        required: False
    password_var:
        description:
        - "Specify password variable name in default logon page (Default= pwd)"
        required: False
    background:
        description:
        - "Field background"
        required: False
        suboptions:
            bgfile:
                description:
                - "Specify background image filename"
            bgstyle:
                description:
                - "'tile'= Tile; 'stretch'= Stretch; 'fit'= Fit; "
            bgcolor_value:
                description:
                - "Specify 6-digit HEX color value"
            bgcolor_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow; "
    passcode_var:
        description:
        - "Specify passcode variable name in default logon page (Default= passcode)"
        required: False
    fail_msg_cfg:
        description:
        - "Field fail_msg_cfg"
        required: False
        suboptions:
            fail_font_custom:
                description:
                - "Specify custom font"
            fail_color:
                description:
                - "Specify font color (Default= red)"
            fail_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana; "
            fail_size:
                description:
                - "Specify font size (Default= 5)"
            fail_msg:
                description:
                - "Configure login failure message in default logon page"
            fail_text:
                description:
                - "Specify login failure message (Default= Invalid username or password. Please try again.)"
            fail_color_value:
                description:
                - "Specify 6-digit HEX color value"
            fail_font:
                description:
                - "Sepcify font (Default= Arial)"
            fail_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow; "
            authz_fail_msg:
                description:
                - "Configure authorization failure message in default logon page, its text attributes follow fail-msg's (Specify authorization failure message (Default= Authorization failed. Please contact your system administrator.))"
    password_cfg:
        description:
        - "Field password_cfg"
        required: False
        suboptions:
            pass_color_value:
                description:
                - "Specify 6-digit HEX color value"
            password:
                description:
                - "Configure password text in default logon page"
            pass_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow; "
            pass_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana; "
            pass_font_custom:
                description:
                - "Specify custom font"
            pass_size:
                description:
                - "Specify font size (Default= 3)"
            pass_text:
                description:
                - "Specify password text (Default= Password)"
            pass_font:
                description:
                - "Sepcify font (Default= Arial)"
            pass_color:
                description:
                - "Specify font color (Default= black)"
    enable_passcode:
        description:
        - "Enable passcode field in default logon page"
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
AVAILABLE_PROPERTIES = ["action_url","background","enable_passcode","fail_msg_cfg","passcode_cfg","passcode_var","password_cfg","password_var","submit_text","username_cfg","username_var","uuid",]

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
        action_url=dict(type='str',),
        submit_text=dict(type='str',),
        passcode_cfg=dict(type='dict',passcode_font_custom=dict(type='str',),passcode_face=dict(type='str',choices=['Arial','Courier_New','Georgia','Times_New_Roman','Verdana']),passcode_color=dict(type='bool',),passcode_text=dict(type='str',),passcode_color_value=dict(type='str',),passcode_color_name=dict(type='str',choices=['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy','olive','orange','purple','red','silver','teal','white','yellow']),passcode_font=dict(type='bool',),passcode=dict(type='bool',),passcode_size=dict(type='int',)),
        username_cfg=dict(type='dict',username=dict(type='bool',),user_font=dict(type='bool',),user_text=dict(type='str',),user_size=dict(type='int',),user_color_value=dict(type='str',),user_font_custom=dict(type='str',),user_color=dict(type='bool',),user_face=dict(type='str',choices=['Arial','Courier_New','Georgia','Times_New_Roman','Verdana']),user_color_name=dict(type='str',choices=['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy','olive','orange','purple','red','silver','teal','white','yellow'])),
        username_var=dict(type='str',),
        password_var=dict(type='str',),
        background=dict(type='dict',bgfile=dict(type='str',),bgstyle=dict(type='str',choices=['tile','stretch','fit']),bgcolor_value=dict(type='str',),bgcolor_name=dict(type='str',choices=['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy','olive','orange','purple','red','silver','teal','white','yellow'])),
        passcode_var=dict(type='str',),
        fail_msg_cfg=dict(type='dict',fail_font_custom=dict(type='str',),fail_color=dict(type='bool',),fail_face=dict(type='str',choices=['Arial','Courier_New','Georgia','Times_New_Roman','Verdana']),fail_size=dict(type='int',),fail_msg=dict(type='bool',),fail_text=dict(type='str',),fail_color_value=dict(type='str',),fail_font=dict(type='bool',),fail_color_name=dict(type='str',choices=['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy','olive','orange','purple','red','silver','teal','white','yellow']),authz_fail_msg=dict(type='str',)),
        password_cfg=dict(type='dict',pass_color_value=dict(type='str',),password=dict(type='bool',),pass_color_name=dict(type='str',choices=['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy','olive','orange','purple','red','silver','teal','white','yellow']),pass_face=dict(type='str',choices=['Arial','Courier_New','Georgia','Times_New_Roman','Verdana']),pass_font_custom=dict(type='str',),pass_size=dict(type='int',),pass_text=dict(type='str',),pass_font=dict(type='bool',),pass_color=dict(type='bool',)),
        enable_passcode=dict(type='bool',),
        uuid=dict(type='str',)
    ))
   
    # Parent keys
    rv.update(dict(
        portal_name=dict(type='str', required=True),
    ))

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authentication/portal/{portal_name}/logon"

    f_dict = {}
    f_dict["portal_name"] = module.params["portal_name"]

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/portal/{portal_name}/logon"

    f_dict = {}
    f_dict["portal_name"] = module.params["portal_name"]

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
        for k, v in payload["logon"].items():
            if v.lower() == "true":
                v = 1
            elif v.lower() == "false":
                v = 0
            if existing_config["logon"][k] != v:
                if result["changed"] != True:
                    result["changed"] = True
                existing_config["logon"][k] = v
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
    payload = build_json("logon", module)
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
    payload = build_json("logon", module)
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