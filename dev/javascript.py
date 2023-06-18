#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : https://wiki.archlinux.org/title/node.js
"""


import subprocess
import sys


class JavaScript():


    @staticmethod
    def install():
        cmd = f'sudo pacman -S --noconfirm npm'
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(f'[-] Python modules, {err}')
            sys.exit(1)

    @staticmethod
    def modules():
        cmd = f'install npm install -g live-server'
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(f'[-] Python modules, {err}')
            sys.exit(1)


j = JavaScript
j.install()
j.modules()
