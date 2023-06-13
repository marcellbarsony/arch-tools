#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : 12 June 2023
Desc  : Rust setup
"""


import os
import shutil
import subprocess


class Rust():

    """Docstring for Rust setup"""

    @staticmethod
    def toolchain():
        """
        Rust default toolchain install
        https://rustup.rs/
        """

        cmd = "rustup default stable"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] Toolchain install')
        except subprocess.CalledProcessError as err:
            print('[-] Toolchain install', err)


    @staticmethod
    def rustup_move(user: str):
        rustup_dir = f'/home/{user}/.rustup'
        new_dir = f'/home/{user}/.local/share/rustup/'

        if os.path.exists(rustup_dir):
            shutil.move(rustup_dir, new_dir)
            print('[+] Move rustup to XDG')
        else:
            print('[-] Move rustup to XDG')


if __name__ == '__main__':
    user = os.getlogin()
    r = Rust()
    r.rustup_move(user)
