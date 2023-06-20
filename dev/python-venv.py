#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Virtual environment helper
"""


import argparse
import os
import subprocess
import sys


class Virtualenv():

    """
    Docstring for Virtualenv
    https://wiki.archlinux.org/title/python
    https://wiki.archlinux.org/title/python/virtual_environment
    https://docs.python.org/3/tutorial/venv.html
    """

    @staticmethod
    def activate():
        # Check if directory exists
        cmd = 'source .venv/bin/activate'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f'[+] Activated venv')
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def create():
        dir = '.venv'
        if not os.path.exists(dir):
            cmd = 'python -m venv .venv'
            try:
                subprocess.run(cmd, shell=True, check=True)
                print(f'[+] Create venv: {dir}')
            except subprocess.CalledProcessError as err:
                print(err)
                sys.exit(1)
        else:
            print('[-] Virtualenv already exists')

    @staticmethod
    def deactivate():
        cmd = 'deactivate'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f'[+] Deactivated venv')
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def freeze():
        cmd = 'python -m pip freeze > requirements.txt'
        try:
            subprocess.run(cmd, shell=True, check=True)
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
    def pip_list():
        cmd = 'python -m pip list'
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='venv.py',
        description='Virtual environment helper',
        epilog='TODO'
        )

    parser.add_argument('-a', '--activate', action='store_true', help='Activate venv')
    parser.add_argument('-c', '--create', action='store_true', help='Create venv')
    parser.add_argument('-d', '--deactivate', action='store_true', help='Deactivate venv')
    parser.add_argument('-f', '--freeze', action='store_true', help='Freeze to requirements')
    parser.add_argument('-i', '--install', action='store_true', help='Install requirements')
    parser.add_argument('-l', '--list', action='store_true', help='List venv packages')

    args = parser.parse_args()

    v = Virtualenv()
    if args.arg1:
        v.activate()
    if args.arg2:
        v.create()
    if args.arg3:
        v.deactivate()
    if args.arg4:
        v.freeze()
    if args.arg5:
        v.install()
    if args.arg6:
        v.pip_list()
