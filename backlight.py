#!/usr/bin/env python3
"""
Author: Name
Date  : 05/27/23
Desc  : Backlight
"""


import subprocess

class Menu():

    """Docstring for Menu"""

    def __init__(self):
        pass

    @staticmethod
    def display_menu():
        print('[1] 10%')
        print('[2] 20%')
        print('[3] 30%')
        print('[4] 40%')
        print('[5] 50%')
        print('[6] 60%')
        print('[7] 70%')
        print('[8] 80%')
        print('[9] 90%')
        print('[0] 100%')

    @staticmethod
    def user_input() -> int:
        while True:
            select = input('> ')
            if select.isdigit() and 0 <= int(select) <= 9:
                if int(select) == 0:
                    brightness = 24242
                else:
                    brightness = int(select) * 2424
                return brightness


class Backlight():

    """
    Docstring for Backlight
    https://wiki.archlinux.org/title/backlight
    """

    def __init__(self):
        pass

    @staticmethod
    def backlight_dir() -> str:
        cmd = 'ls /sys/class/backlight/'
        out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
        return out.stdout.strip()

    @staticmethod
    def backlight_set(brightness: str, backlight_dir: str):
        cmd = f'sudo echo {brightness} > /sys/class/backlight/{backlight_dir}/brightness'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)


if __name__ == '__main__':
    m = Menu()
    m.display_menu()
    brightness = m.user_input()

    b = Backlight()
    dir = b.backlight_dir()
    b.backlight_set(str(brightness), dir)
