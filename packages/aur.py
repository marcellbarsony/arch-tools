#.!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Install AUR packages
"""


import subprocess
import sys


aur_helper = 'pikaur'


def packages_get():
    packages = ''
    with open('_packages_aur.ini', 'r') as file:
        for line in file:
            if not line.startswith('[') and not line.startswith('#') and line.strip() != '':
                packages += f'{line.rstrip()} '
    return packages

def packages_install(aur_helper: str, packages: str):
    cmd = f'{aur_helper} -S --noconfirm {packages}'
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print('[-] AUR Install', err)
        sys.exit(1)

if __name__ == "__main__":
    packages = packages_get()
    packages_install(aur_helper, packages)
