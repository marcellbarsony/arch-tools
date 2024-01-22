#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : October 2023
Desc  : Firefox config setup script
"""


import os
from os.path import exists
import shutil
import subprocess
import sys


USER = os.getlogin()
CWD = os.getcwd()


def get_user_profile():
    firefox_conf = f"/home/{USER}/.mozilla/firefox/"
    for directory in os.listdir(firefox_conf):
        if "default-release" in directory:
            return directory


class Containers():

    """Docstring for Containers"""

    @staticmethod
    def containers():
        src = f"/home/{USER}/.config/firefox/containers/containers.json"
        dst = f"/home/{USER}/.mozilla/firefox/{get_user_profile()}/containers.json"
        shutil.copy2(src, dst)

c = Containers()
c.containers()


class Arkenfox():

    """Docstring for Arkenfox"""

    @staticmethod
    def clone():
        dst = f"/home/{USER}/Downloads/arkenfox"
        cmd = f"git clone git@github.com:arkenfox/user.js {dst}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        except Exception:
            sys.exit(1)

    @staticmethod
    def overrides_copy():
        src = f"/home/{USER}/.config/firefox/preferences/user-overrides.js"
        dst = f"/home/{USER}/.mozilla/firefox/{get_user_profile()}/user-overrides.js"
        shutil.copy2(src, dst)

    @staticmethod
    def arkenfox_copy():
        src = f"/home/{USER}/Downloads/arkenfox/user.js"
        dst = f"/home/{USER}/.mozilla/firefox/{get_user_profile()}"
        print(src)
        print(dst)
        for file in os.listdir(src):
            if file != ".git" and file != ".github":
                shutil.copy(os.path.join(src, file), os.path.join(dst, file))


if __name__ == "__main__":
    a = Arkenfox()
    a.clone()
