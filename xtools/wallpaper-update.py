#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Set random wallpaper to active X11 displays
"""


import os
import shutil
import urllib.request
import zipfile


user = 'marci'
dir = f'/home/{user}/Pictures'
url = 'https://www.dropbox.com/sh/eo65dcs7buprzea/AABSnhAm1sswyiukCDW9Urp9a?dl=1'
out = f'{dir}/wallpapers.zip'


def directory(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir, ignore_errors=True)
        print('[+] Removing directory')
        os.mkdir(dir)
        print('[+] Creating directory')
    else:
        os.mkdir(dir)
        print('[+] Creating directory')

def download(out: str, url: str):
    print('[+] Downloading...')
    urllib.request.urlretrieve(url, out)

def unzip(out: str, dir: str):
    with zipfile.ZipFile(out, 'r') as zip_ref:
        zip_ref.extractall(dir)
    print('[+] Unzipping')
    os.remove(out)
    print('[+] Removing zip')


directory(dir)
download(out, url)
unzip(out, dir)
