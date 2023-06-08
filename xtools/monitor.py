#!/usr/bin/env python3
"""
Author: Name
Date  : 05/13/23
Desc  : Display setup tool
"""

import subprocess

result = subprocess.run('xrandr', capture_output=True, text=True)

for line in result.stdout.splitlines():
    words = line.split()
    if len(words) > 1 and words[1] == "connected":
        display_name = words[0]
        print("Display connected:", display_name)
