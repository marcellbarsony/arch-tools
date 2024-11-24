#!/usr/bin/env python3
"""
Pacman mirrorlist backup & update
"""


import subprocess
import sys


def backup():
    src = "/etc/pacman.d/mirrorlist"
    dst = "/etc/pacman.d/mirrorlist.bak"
    cmd = f"sudo cp {src} {dst}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        print(":: [-] :: PACMAN :: Backup ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: PACMAN :: Backup")

def update():
    cmd = "sudo reflector \
        --latest 25 \
        --protocol https \
        --connection-timeout 5 \
        --sort rate \
        --save /etc/pacman.d/mirrorlist"
    try:
        print(":: [i] :: PACMAN :: Mirrorlist update")
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        print(":: [-] :: PACMAN :: Mirrorlist ::", err)
    else:
        print(":: [+] :: PACMAN :: Mirrorlist")


if __name__ == "__main__":
    backup()
    update()
