#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : NVIM Python DAP setup
"""


import argparse
import os
import subprocess
import sys


user = os.getlogin()
venv = 'debugpy'


class Debugpy():

    @staticmethod
    def dir(user: str):
        dir = f'/home/{user}/.local/venv'
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)

    @staticmethod
    def virtualenv(venv: str):
        cmd = f'python -m venv {venv}'
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def install(venv: str):
        cmd = f'{venv}/bin/python -m pip install debugpy'
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='python-dap.py',
        description='Virtual environment helper',
        epilog='TODO'
        )

    d = Debugpy()
    d.dir(user)
    d.virtualenv(venv)
    d.install(venv)
