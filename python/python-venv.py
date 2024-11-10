#!/usr/bin/env python3
"""
Docstring for setting up Python virtual environments
https://wiki.archlinux.org/title/python
https://wiki.archlinux.org/title/python/virtual_environment
https://docs.python.org/3/tutorial/venv.html
"""


import os
import subprocess
import sys


USER = os.getlogin()
DIRS = ["arch", "arch-post", "arch-tools"]


def chdir(dir: str):
    os.chdir(f"/home/{USER}/.local/git/{dir}")

def venv_init(dir: str):
    if not os.path.exists(dir):
        cmd = "python -m venv .venv"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)
        else:
            print(":: [+] :: Venv init ::", dir)

def venv_ops():
    cmds = [
        "source .venv/bin/activate",
        "pip install --upgrade pip",
        "python -m pip install -r requirements.txt",
        "deactivate"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(":: [-] :: Venv ops ::", err)
            sys.exit(1)
        else:
            print(":: [+] :: Venv ops ::", cmd)



if __name__ == "__main__":
    for dir in DIRS:
        chdir(dir)
        venv_init(dir)
        venv_ops()
