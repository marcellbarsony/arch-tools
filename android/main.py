#!/usr/bin/env python3
"""
Android tools
"""

import subprocess
import sys


def android_install():
    cmd = "sudo pacman -S --noconfirm android-tools scrcpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print(":: [-] :: Android tools :: Install ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: Android tools :: Install")


if __name__ == "__main__":
    android_install()
