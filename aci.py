'''
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
'''

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


APIC_URL = ""
APIC_USERNAME = ""
APIC_PASSWORD = ""

base_url = "https://{}/api/".format(APIC_URL)
cookies = {}

def apic_login():
    credentials = {'aaaUser':
                    {'attributes':
                        {'name': APIC_USERNAME, 'pwd': APIC_PASSWORD }
                    }
        }

    url = base_url + 'aaaLogin.json'

    json_credentials = json.dumps(credentials)

    response = requests.post(url, data=json_credentials, verify=False)

    print(response.json())
    if "aaaLogin" in response.json()['imdata'][0]:
        cookies['APIC-Cookie'] =  response.json()['imdata'][0]['aaaLogin']['attributes']['token']
        print("The cookie is: {}".format(cookies['APIC-Cookie']) )
    else:
        print("It's not working")

def get_aci_tenants():
    url = base_url + "node/class/fvTenant.json"

    response = requests.get(url, cookies=cookies, verify=False)

    return response.json()["imdata"]

def get_aci_endpoints():
    url = base_url + "node/class/fvCEp.json?rsp-subtree=children"

    response = requests.get(url, cookies=cookies, verify=False)

    return response.json()["imdata"]

def get_aci_interfaces():
    url = base_url + "node/class/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf"
    
    response = requests.get(url, cookies=cookies, verify=False)

    return response.json()["imdata"]