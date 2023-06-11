#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Set random wallpaper to active X11 displays
"""


import getpass
import os
import random
import subprocess


class Display():

    """Docstring for Displays"""

    @staticmethod
    def get_displays() -> list:
        result = subprocess.run('xrandr', capture_output=True, text=True)
        displays = []
        for line in result.stdout.splitlines():
            words = line.split()
            if len(words) > 1 and words[1] == "connected":
                display_name = words[0]
                displays.append(display_name)
        return displays

    @staticmethod
    def remove_display(displays: list):
        if len(displays) > 1:
            for display in displays:
                if display == 'eDP1' or display == 'eDP-1':
                    subprocess.run(f'xrandr --output {display} --off', shell=True)
                    displays.remove(display)
        return displays


class Wallpaper():

    """Docstring for Wallpaper"""

    def __init__(self):
        self.user = getpass.getuser()
        self.path = f'/home/{self.user}/Pictures'

    def get_files(self) -> list:
        files = []
        for root, _, filenames in os.walk(self.path):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files

    @staticmethod
    def get_random(files: list) -> str:
        file = random.choice(files)
        return file

    @staticmethod
    def set_wallpaper(displays: list, file: str):
        for display in displays:
            cmd = f'xwallpaper --output {display} --stretch {file}'
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    m = Display()
    displays = m.get_displays()
    displays = m.remove_display(displays)
    w = Wallpaper()
    files = w.get_files()
    file = w.get_random(files)
    w.set_wallpaper(displays, file)
    print('[+] Set wallpaper ' + str(displays))
