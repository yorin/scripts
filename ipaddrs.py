#!/usr/bin/python
from netaddr import *
import pprint
# -*- coding: utf-8 -*-

from netaddr import *
import pprint

ip = IPAddress('192.0.2.1')
print "version: IPV%d"%ip.version
print "binary: %s"%ip.bits()

for ip in IPNetwork('192.0.2.0/23'):
  print '%s' % ip
ip_list = [ip for ip in IPNetwork('192.0.2.0/23')]
print '%s' % len(ip_list)
