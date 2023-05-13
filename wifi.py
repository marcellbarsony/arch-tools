#!/usr/bin/env python3
"""
Author: Name
Date  : 05/13/23
Desc  : Description
"""

import getpass
import subprocess

wifi_ssid = input('Wi-Fi SSID: ')
wifi_pass = getpass.getpass('Wi-Fi pass: ')

cmd = f'nmcli device wifi connect {wifi_ssid} password {wifi_pass}'
subprocess.run(cmd, shell=True, check=True)
