# -*- coding: utf-8 -*-
"""
IP Address information for eth0

"""

import subprocess as sp
import json

ipa = sp.run(['ip', '-json', 'addr', 'show', 'eth0'], capture_output=True)
'''
Out[25]: CompletedProcess(args=['ip', '-json', 'addr', 'show', 'eth0'], 
returncode=0, 
stdout=b'[{"ifindex":11,"ifname":"eth0",
"flags":["BROADCAST","MULTICAST","UP","LOWER_UP"],
"mtu":1500,"qdisc":"mq","operstate":"UP","group":"default",
"txqlen":1000,"link_type":"ether","address":"30:9c:23:b6:0e:38",
"broadcast":"ff:ff:ff:ff:ff:ff",
"addr_info":[{"family":"inet","local":"192.168.1.84","prefixlen":24,
              "broadcast":"192.168.1.255","scope":"global",
              "noprefixroute":true,"label":"eth0",
              "valid_life_time":4294967295,"preferred_life_time":4294967295},
             {"family":"inet6","local":"2600:1700:5026:4150::42","prefixlen":128,
              "scope":"global","dynamic":true,"noprefixroute":true,
              "valid_life_time":3266,"preferred_life_time":3266},
             {"family":"inet6","local":"2600:1700:5026:4150:6d96:5495:adfb:ffda",
              "prefixlen":64,"scope":"global","dynamic":true,"noprefixroute":true,
              "valid_life_time":3036,"preferred_life_time":3036},
             {"family":"inet6","local":"fe80::6d18:b785:b17f:3a55","prefixlen":64,
              "scope":"link","noprefixroute":true,"valid_life_time":4294967295,
              "preferred_life_time":4294967295}]}]\n', 
stderr=b'')
'''
ipa_j = json.loads(ipa.stdout)
# get 'local' addresses

for d in ipa_j[0]['addr_info']:
   print(d['local'])
     