#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Install AUR packages
"""


import configparser
import subprocess
import sys


def packages_get():
    packages = ""
    with open("_packages_aur.ini", "r") as file:
        for line in file:
            if not line.startswith("[") and not line.startswith("#") and line.strip() != "":
                packages += f"{line.rstrip()} "
    return packages

def packages_install(packages: str, aurhelper: str):
    cmd = f"{aurhelper} -S --noconfirm {packages}"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print("[-] AUR Install", err)
        sys.exit(1)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    aurhelper = config.get("aur", "aurhelper")

    packages = packages_get()
    packages_install(packages, aurhelper)
