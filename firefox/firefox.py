#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : 19 October 2023
Desc  : Firefox setup script
"""


import os
import shutil
import subprocess

USER = os.getlogin()
CWD = os.getcwd()

def get_user_profile():
    firefox_conf = f"/home/{USER}/.mozilla/firefox/"
    for directory in os.listdir(firefox_conf):
        if "default-release" in directory:
            return directory

# Containers

# Arkenfox

def arkenfox_clone():
    cmd = "git clone git@github.com:arkenfox/user.js/"
    subprocess.run(cmd, shell=True)

def arkenfox_copy():
    src = CWD + "/user.js"
    dst = f"/home/{USER}/.mozilla/firefox/{get_user_profile()}"
    print(src)
    print(dst)
    for file in os.listdir(src):
        if file != ".git" and file != ".github":
            shutil.copy(os.path.join(src, file), os.path.join(dst, file))

def name():
    files = [
        "updater.sh",
        "user.js",
        "user-overrides.js"
    ]
    for file in files:
        src = f"/home/{USER}/.config/firefox/preferences/{file}"
        dst = f"/home/{USER}/.mozilla/firefox/{get_user_profile()}/"
        print(src)
        print(dst)

#name()
arkenfox_copy()
