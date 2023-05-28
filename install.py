#!/usr/bin/env python3
"""
Author: Name
Date  : 05/24/23
Desc  : Description
"""


import getpass
import subprocess
import sys


def install(package: str):
    cmd = f'sudo pacman -S --noconfirm {package}'
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print('[-] Install', err)
        sys.exit(1)

def add_group(user: str):
    cmd = f'usermod -aG {user} wireshark'
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print('[-] Install', err)
        sys.exit(1)


packages = [
    # netcat
    'gnu-netcat',
    # nmap
    'nmap',
    # wireshark
    'wireshark',
    'adwaita-qt5',
    # web server scanner
    'nikto',
    ]

for package in packages:
    install(package)

add_group(getpass.getuser())
