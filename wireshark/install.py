#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : October 2023
Desc  : Install Wireshark
"""


import getpass
import subprocess
import sys


PACKAGES = [
    "wireshark-qt",
    "qt5ct"
    ]

PACKAGES_AUR = [
    "adwaita-qt5-git",
    "adwaita-qt6-git"
    ]

def install():
    for package in PACKAGES:
        cmd = f"sudo pacman -S --noconfirm {package}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except Exception as err:
            print("[-] Install", err)
            sys.exit(1)

def install_aur():
    for package in PACKAGES_AUR:
        cmd = f"paru -S --noconfirm {package}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except Exception as err:
            print("[-] Install", err)
            sys.exit(1)

def group_add(user: str):
    groups = "wireshark"
    cmd = f"sudo usermod -aG {groups} {user}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Group add: {groups}")
    except Exception as err:
        print("[-] Group add", err)
        sys.exit(1)


if __name__ == "__main__":
    user = getpass.getuser()
    install()
    install_aur()
    group_add(user)
    print("[INFO] Please reboot to apply the changes")
