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


from datetime import datetime
from sqlalchemy import create_engine
from models import Base, Tenant, Endpoint, PhysicalInterface
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import yaml
import aci as aci

DATABASE_URL = 'postgres+psycopg2://myUsername:myPassword@localhost:5432/ACI'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    recreate_database()

    aci.apic_login()

    '''
    tenants = aci.get_aci_tenants()

    
    for tenant in tenants:
        #print(tenant)
        tenant = tenant["fvTenant"]["attributes"]
        newTenant = Tenant(
                name=tenant["name"],    
                descr=tenant["descr"],
                dn=tenant["dn"],
        )
        with session_scope() as s:
            s.add(newTenant)

    
    endpoints = aci.get_aci_endpoints()

    for endpoint in endpoints:
        # print(endpoint)
        
        endpoint = endpoint["fvCEp"]

        newEndpoint = Endpoint(
                ip=endpoint["attributes"]["ip"],    
                mac=endpoint["attributes"]["mac"],
                dn=endpoint["attributes"]["dn"],
                encap=endpoint["attributes"]["encap"],
                #targetDn=endpoint["children"]["targetDn"],
                #targetClass=endpoint["children"]["targetClass"],
                
        )

        print(newEndpoint)
    '''
    interfaces = aci.get_aci_interfaces()

    
    for interface in interfaces:
        #print(tenant)
        interface = interface["l1PhysIf"]["attributes"]
        newInterface = PhysicalInterface(
                adminSt=interface["adminSt"],    
                portT=interface["portT"],
                dn=interface["dn"],
                usage=interface["usage"],
        )
        with session_scope() as s:
            s.add(newInterface)

