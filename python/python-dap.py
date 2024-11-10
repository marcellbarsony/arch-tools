#!/usr/bin/env python3
"""
Nvim Python DAP setup
"""


import os
import subprocess
import sys


USER = os.getlogin()
VENV = "debugpy"
VENV_PATH = f"/home/{USER}/.local/share/python/{VENV}"


def venv_init():
    cmd = f"python -m venv {VENV_PATH}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] :: Venv :: Init")
    except subprocess.CalledProcessError as err:
        print(err)
        sys.exit(1)

def venv_ops():
    cmds = [
        f"source {VENV_PATH}/bin/activate",
        "pip install --upgrade pip",
        "pip install debugpy"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)
        else:
            print(":: [+] :: Venv ::", cmd)


if __name__ == "__main__":
    venv_init()
    venv_ops()
