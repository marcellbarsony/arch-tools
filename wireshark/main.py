#!/usr/bin/env python3
"""
Wireshark setup
"""


import getpass
import subprocess
import sys


PACKAGES = [
    "wireshark-qt",
    "qt5ct"
]

def install(packages: list):
    for package in packages:
        cmd = f"sudo pacman -S --noconfirm {package}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except Exception as err:
            print(":: [-] :: Install ::", err)
            sys.exit(1)

def group_add(user: str):
    groups = "wireshark"
    cmd = f"sudo usermod -aG {groups} {user}"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print(":: [-] :: Group add ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: Group add ::", groups)


if __name__ == "__main__":
    user = getpass.getuser()
    install(PACKAGES)
    group_add(user)
    print(":: [i] :: Please reboot to apply the changes")
