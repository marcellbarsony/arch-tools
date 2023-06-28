#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Rust setup
"""


import os
import shutil


user = os.getlogin()


class Rust():

    """Docstring for Rust setup"""

    # Check Rustup version
    # rustc --version

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
    r = Rust()
    r.rustup_move(user)
