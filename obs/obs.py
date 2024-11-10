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
        "sudo pacman -S --noconfirm obs-studio",
        "paru -S --noconfirm obs-pipewire-audio-capture-bin"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(":: [-] :: OBS :: Install ::", err)
            sys.exit(1)
        else:
            print(":: [+] :: OBS :: Install")


if __name__ == "__main__":
    obs_install()
