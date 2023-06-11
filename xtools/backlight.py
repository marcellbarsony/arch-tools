#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 23
Desc  : Set X backlight
Deps  : brightnessctl
"""


import subprocess


class Menu():

    """Docstring for Menu"""

    @staticmethod
    def display_menu():
        print('Int: 0-10 [0-100%]')

    @staticmethod
    def user_input() -> int:
        while True:
            select = input('> ')
            if select.isdigit() and 0 <= int(select) <= 10:
                brightness = int(select) * 25
                return brightness


class Backlight():

    """
    Docstring for Backlight
    https://wiki.archlinux.org/title/backlight
    """

    @staticmethod
    def backlight_set(value: int):
        cmd = f'brightnessctl --class=backlight set {value}'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)


if __name__ == '__main__':
    m = Menu()
    m.display_menu()
    value = m.user_input()

    b = Backlight()
    b.backlight_set(value)
