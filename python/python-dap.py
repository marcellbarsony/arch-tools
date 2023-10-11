#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : NVIM Python DAP setup
"""


import os
import subprocess
import sys


USER = os.getlogin()
VENV = "debugpy"
VENV_PATH = f"/home/{USER}/.local/share/python/{VENV}"


class Debugpy():

    @staticmethod
    def venv_init():
        cmd = f"python -m venv {VENV_PATH}"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"[+] Venv init")
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def venv_ops():
        cmd1 = f"source {VENV_PATH}/bin/activate && "
        cmd2 = "pip install --upgrade pip && "
        cmd3 = "pip install debugpy"
        cmd = cmd1 + cmd2 + cmd3
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Venv activation")
            print("[+] Pip upgrade")
            print("[+] Debugpy install")
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)


if __name__ == "__main__":
    d = Debugpy()
    d.venv_init()
    d.venv_ops()
