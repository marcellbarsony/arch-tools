#!/usr/bin/env python3
"""
Author: Name
Date  : 05/13/23
Desc  : Wallpaper tool
"""


import getpass
import os
import random
import subprocess


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
    def set_wallpaper(file: str):
        cmd = f'xwallpaper --output HDMI2 --maximize {file}'
        subprocess.run(cmd, shell=True)
        cmd = f'xwallpaper --output DP1 --maximize {file}'
        subprocess.run(cmd, shell=True)


w = Wallpaper()
files = w.get_files()
file = w.get_random(files)
w.set_wallpaper(file)
