#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : JavaScript / Node.js environment setup
Docs  : https://wiki.archlinux.org/title/node.js
"""


import subprocess
import sys


class JavaScript():

    @staticmethod
    def install():
        cmd = f"sudo pacman -S --noconfirm npm"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"[+] NPM install")
        except subprocess.CalledProcessError as err:
            print(f"[-] NPM install, {err}")
            sys.exit(1)

    @staticmethod
    def modules():
        """https://www.npmjs.com/package/live-server"""
        cmd = f"npm install -g live-server"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] NPM install: live-server")
        except subprocess.CalledProcessError as err:
            print(f"[-] NPM install: live-server, {err}")
            sys.exit(1)


if __name__ == "__main__":
    j = JavaScript
    j.install()
    j.modules()
