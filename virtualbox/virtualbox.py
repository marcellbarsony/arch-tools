#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : October 2023
Desc  : Install VirtualBox
"""


import getpass
import subprocess
import sys


PACKAGES = [
    "virtualbox",
    "virtualbox-host-dkms"
]

def install():
    for package in PACKAGES:
        cmd = f"sudo pacman -S --noconfirm {package}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except Exception as err:
            print("[-] Install", err)
            sys.exit(1)

def group_add(user: str):
    group = "vboxusers"
    cmd = f"sudo usermod -aG {group} {user}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Group add: {group}")
    except Exception as err:
        print("[-] Group add", err)
        sys.exit(1)

def kernel_module():
    module = "vboxdrv"
    cmd = f"sudo modprobe {module}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Modprobe: {module}")
    except Exception as err:
        print(f"[-] Modprobe", err)
        sys.exit(1)


if __name__ == "__main__":
    user = getpass.getuser()
    install()
    group_add(user)
    kernel_module()
    print("[I] Please reboot to apply the changes")
