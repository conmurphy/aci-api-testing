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


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Tenant(Base):
    __tablename__ = 'tenant'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    descr = Column(String)
    dn = Column(String)
    

    def __repr__(self):
        return "<Tenant(name='{}', descr='{}', dn={})>"\
                .format(self.name, self.descr, self.dn)

class Endpoint(Base):
    __tablename__ = 'endpoints'
    id = Column(Integer, primary_key=True)
    mac = Column(String)
    ip = Column(String)
    dn = Column(String)
    encap = Column(String)
    targetClass = Column(String)
    targetDn = Column(String)

    def __repr__(self):
        return "<Endpoint(mac='{}', ip='{}', dn={}, encap={}, targetClass={}, targetDn={})>"\
                .format(self.mac, self.ip, self.dn, self.encap, self.targetClass, self.targetDn)

class PhysicalInterface(Base):
    __tablename__ = 'physical_interface'
    id = Column(Integer, primary_key=True)
    portT = Column(String)
    usage = Column(String)
    dn = Column(String)
    adminSt = Column(String)

    def __repr__(self):
        return "<PhysicalInterface(portT='{}', usage='{}', dn={}, adminSt={})>"\
                .format(self.portT, self.usage, self.dn, self.adminSt)