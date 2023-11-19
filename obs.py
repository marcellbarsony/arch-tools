#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : October 2023
Desc  : OBS install
"""

import subprocess
import sys


def obs_install():
    cmds = [
        "sudo pacman -S --noconfirm obs",
        "paru -S --noconfirm obs-pipewire-audio-capture-bin"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(f"[-] OBS install, {err}")
            sys.exit(1)
        print(f"[+] OBS install")


if __name__ == "__main__":
    obs_install()
