#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Python virtual environment setup
"""


import os
import subprocess
import sys


USER = os.getlogin()
DIRS = ["arch", "arch-post", "arch-tools"]


class Virtualenv():

    """
    Docstring for setting up Python virtual environments
    https://wiki.archlinux.org/title/python
    https://wiki.archlinux.org/title/python/virtual_environment
    https://docs.python.org/3/tutorial/venv.html
    """

    @staticmethod
    def chdir(user: str, dir: str):
        os.chdir(f"/home/{user}/.local/git/{dir}")

    @staticmethod
    def venv_init(dir: str):
        if not os.path.exists(dir):
            cmd = "python -m venv .venv"
            try:
                subprocess.run(cmd, shell=True, check=True)
                print(f"[+] Venv init: {dir}")
            except subprocess.CalledProcessError as err:
                print(err)
                sys.exit(1)

    @staticmethod
    def venv_ops():
        cmd1 = "source .venv/bin/activate && "
        cmd2 = "pip install --upgrade pip && "
        cmd3 = "python -m pip install -r requirements.txt && "
        cmd4 = "deactivate"
        cmd =  cmd1 + cmd2 + cmd3 + cmd4
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Venv operations")
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)


if __name__ == "__main__":
    v = Virtualenv()
    for dir in DIRS:
        v.chdir(USER, dir)
        v.venv_init(dir)
        v.venv_ops()
