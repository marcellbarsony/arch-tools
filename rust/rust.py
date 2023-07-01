#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Rust setup
"""


import os
import shutil
import subprocess


USER = os.getlogin()


class Rust():

    """
    Docstring for Rust setup
    https://wiki.archlinux.org/title/Rust
    """

    @staticmethod
    def toolchain():
        """Rust default toolchain install"""
        cmd = "rustup default stable"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] Toolchain install')
        except subprocess.CalledProcessError as err:
            print('[-] Toolchain install', err)

    @staticmethod
    def xdg_standard(user: str):
        """XDG directory standard"""
        dir = f"/home/{user}/.rustup"
        dir_new = f"/home/{user}/.local/share/rustup/"
        if os.path.exists(dir):
            shutil.move(dir, dir_new)
            print("[+] Move rustup to XDG")

if __name__ == "__main__":
    r = Rust()
    r.toolchain()
    r.xdg_standard(USER)
