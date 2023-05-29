#!/usr/bin/env python3
"""
Author: Name
Date  : 05/27/23
Desc  : Font management tool
"""


import subprocess


class Menu():

    """Docstring for Menu"""

    def __init__(self):
        pass

    @staticmethod
    def display_menu():
        print('[1] Show installed')
        print('[2] Show font families')

    @staticmethod
    def user_input() -> int:
        while True:
            select = input('> ')
            if select.isdigit() and 1<= int(select) <= 2:
                return int(select)


class FontTools():

    """Docstring for FontTools"""

    def __init__(self):
        pass

    @staticmethod
    def get_installed():
        cmd =  'fc-list | grep -ioE ": [^:]*$1[^:]+:" | sed -E "s/(^: |:)//g" | tr , \\n | sort | uniq'
        subprocess.run(cmd, shell=True)

    @staticmethod
    def fc_match(font: str):
        cmd =  f'fc-match {font}'
        out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
        return out.stdout.strip()


if __name__ == '__main__':
    m = Menu()
    m.display_menu()
    select = m.user_input()

    f = FontTools()
    if select == 1:
        f.get_installed()
    if select == 2:
        sans = f.fc_match('sans')
        print('Sans: ', sans)
        sans_serif = f.fc_match('sans-seif')
        print('Sans-Serif: ', sans_serif)
        monospace = f.fc_match('monospace')
        print('Monospace: ', monospace)
