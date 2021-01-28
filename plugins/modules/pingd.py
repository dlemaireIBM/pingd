#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2016, Toshio Kuratomi <tkuratomi@ansible.com>
# (c) 2020, Daniel Lemaire for a test
# IDEA: # GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = '''
---
module: ping
version_added: historical
short_description: Try to connect to host, verify a usable python and return C(pong) on success
description:
   - A trivial test module, this module always returns C(pong) on successful
     contact. It does not make sense in playbooks, but it is useful from
     C(/usr/bin/ansible) to verify the ability to login and that a usable Python is configured.
   - This is NOT ICMP ping, this is just a trivial test module that requires Python on the remote-node.
   - For Windows targets, use the M(ansible.windows.win_ping) module instead.
   - For Network targets, use the M(ansible.netcommon.net_ping) module instead.
options:
  data:
    description:
      - Data to return for the C(ping) return value.
      - If this parameter is set to C(crash), the module will cause an exception.
    type: str
    default: pong
seealso:
- module: ansible.netcommon.net_ping
- module: ansible.windows.win_ping
author:
    - Ansible Core Team
    - Michael DeHaan
    - Daniel Lemaire
'''

EXAMPLES = '''
# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m ping

- name: Example from an Ansible Playbook
  ping:

- name: Induce an exception to see what happens
  ping:
    data: crash

 - name: Add a variable for change or not
   ping:
     chg: false
'''

RETURN = '''
ping:
    description: value provided with the data parameter
    returned: success
    type: str
    sample: pong
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='tac'),
            chg=dict(type='bool', default=True)
        ),
        supports_check_mode=True
    )

    result = dict(
        tic=module.params['data'],
        toto=module.params['chg']
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    if module.params['chg']:
        result['changed'] = module.params['chg']

    module.exit_json(**result)


if __name__ == '__main__':
    main()
