#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys


USER = os.getlogin()


def firefox_process():
    cmd = "pgrep firefox"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except Exception:
        return False
    else:
        return True

def firefox_profile_path() -> str:
    path = f"/home/{USER}/.mozilla/firefox"
    for dir_name in os.listdir(path):
        dir_path = os.path.join(path, dir_name)

        if os.path.isdir(dir_path) and "default-release" in dir_path:
            return dir_path

    raise FileNotFoundError(":: [-] :: Cannot find Firefox default profile")

def userChrome(dst: str):
    src = f"/home/{USER}/.config/firefox/chrome/"
    try:
        shutil.copy2(src, dst)
    except Exception as err:
        print(":: [-] :: userChrome :: Copy ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: userChrome :: Copy")

def containers(dst: str):
    src = f"/home/{USER}/.config/firefox/containers/containers.json"
    try:
        shutil.copy2(src, dst)
    except Exception as err:
        print(":: [-] :: Containers :: Copy ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: Containers :: Copy")

def preferences(dst: str):
    src = f"/home/{USER}/.config/firefox/preferences/user.js"
    try:
        shutil.copy2(src, dst)
    except Exception as err:
        print(":: [-] :: Preferences :: Copy ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: Preferences :: Copy")


if __name__ == "__main__":

    if firefox_process():
        raise Exception(":: [-] :: Firefox is already running")

    ff_path = firefox_profile_path()

    userChrome(ff_path)
    containers(ff_path)
    preferences(ff_path)
