#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : 11 June 2023
Desc  : Python setup
"""


import getpass
import os
import subprocess
import sys


class Python():

    """
    Docstring for Python
    https://wiki.archlinux.org/title/python
    https://wiki.archlinux.org/title/python/virtual_environment
    """

    @staticmethod
    def get_modules(cwd: str):
        modules = [] 
        with open(f'{cwd}/packages/python.ini', 'r') as file:
            for line in file:
                if not line.startswith('[') and not line.startswith('#') and line.strip() != '':
                    modules.append(line.rstrip())
        return modules

    @staticmethod
    def modules(modules: list):
        for module in modules:
            cmd = f'pip install {module}'
            try:
                subprocess.run(cmd, shell=True, check=True)
            except subprocess.CalledProcessError as err:
                print(f'[-] Python modules, {err}')
                sys.exit(1)
        print('[+] Python modules')

    @staticmethod
    def venv(user: str):
        dirs = ['arch', 'arch-post', 'arch-tools']
        cmd = 'python -m venv venv'
        for dir in dirs:
            os.chdir(f'/home/{user}/.src/{dir}')
            subprocess.run(cmd, shell=True)
            print(f'[+] Python venv: {dir}')


if __name__ == "__main__":
    p = Python()
    #modules = p.get_modules(os.getcwd())
    #p.modules(modules)
    p.venv(getpass.getuser())
