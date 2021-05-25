#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Display information from the routing table

Created on Mon May 24 23:25:34 2021

@author: keith
"""

import subprocess as sp
import json

ipr = sp.run(args=['ip', '-json', 'route'],capture_output=True)
'''
CompletedProcess(args=['ip', '-json', 'route'], returncode=0, 
                 stdout=b'[{"dst":"default","gateway":"192.168.1.254",
                 "dev":"eth0","protocol":"static","metric":100,"flags":[]},
                 {"dst":"default","gateway":"10.0.0.1",
                  "dev":"wlan0","protocol":"dhcp","metric":600,"flags":[]},
                 {"dst":"10.0.0.0/24","dev":"wlan0","protocol":"kernel",
                  "scope":"link","prefsrc":"10.0.0.37","metric":600,"flags":[]},
                 {"dst":"192.168.1.0/24","dev":"eth0","protocol":"kernel",
                  "scope":"link","prefsrc":"192.168.1.84","metric":100,"flags":[]},
                 {"dst":"192.168.122.0/24","dev":"virbr0","protocol":"kernel",
                  "scope":"link","prefsrc":"192.168.122.1","flags":["linkdown"]}]\n',
                 stderr=b'')
'''
ipr_j = json.loads(ipr.stdout)

# show all routes
print("all routes", end="\n\n")
for d in ipr_j:
    for k in d:
        print(k, ":", d[k])
    print()
    
# Show only default routes 
print("default routes only", end="\n\n")
for d in ipr_j:
    if d["dst"] == "default":
        for k in d:
            print(k, ":", d[k])
    print()   