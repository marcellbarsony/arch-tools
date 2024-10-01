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
    "virtualbox-guest-iso"
    "virtualbox-host-dkms", # Linux kernel
]

def install_check():
    for package in PACKAGES:
        cmd = f"pacman -Q {package}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except Exception:
            print(f":: [i] Installing {package}")
            install(package)

def install(package):
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
    except Exception as err:
        print("[-] Group add", err)
        sys.exit(1)
    else:
        print(f"[+] Group add: {group}")

def kernel_module():
    module = "vboxdrv"
    cmd = f"sudo modprobe {module}"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print(f"[-] Modprobe", err)
        sys.exit(1)
    else:
        print(f"[+] Modprobe: {module}")


if __name__ == "__main__":
    user = getpass.getuser()
    install_check()
    group_add(user)
    kernel_module()
    print("[i] Please reboot to apply the changes")
