#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Python setup
"""


import os
import subprocess
import sys


user = os.getlogin()
dirs = ['arch', 'arch-post', 'arch-tools']


class PythonVenv():

    """
    Docstring for setting up Python virtual environments
    https://wiki.archlinux.org/title/python
    https://wiki.archlinux.org/title/python/virtual_environment
    https://docs.python.org/3/tutorial/venv.html
    """

    @staticmethod
    def chdir(user: str, dir: str):
        os.chdir(f'/home/{user}/.local/git/{dir}')

    @staticmethod
    def create(dir: str):
        if not os.path.exists(dir):
            cmd = 'python -m venv .venv'
            try:
                subprocess.run(cmd, shell=True, check=True)
                print(f'[+] Create venv: {dir}')
            except subprocess.CalledProcessError as err:
                print(err)
                sys.exit(1)

    @staticmethod
    def activate():
        cmd = 'source .venv/bin/activate'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f'[+] Activated venv')
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def install():
        cmd = 'python -m pip install -r requirements.txt'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] Installed requirements')
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def deactivate():
        cmd = 'deactivate'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f'[+] Deactivated venv')
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)


if __name__ == "__main__":
    v = PythonVenv()
    for dir in dirs:
        v.chdir(user, dir)
        v.create(dir)
        v.activate()
        v.install()
        v.deactivate()
