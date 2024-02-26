#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : 02/08/24
Desc  : Remove orphaned snapshots
"""

import subprocess

for number in range(1, 1000):
    try:
        path = f"/home/.snapshots/{number}/snapshot"
        cmd = f"sudo btrfs subvolume delete {path}"
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print(f"[+] Removing snapshot {number} - {path}")
    except Exception:
        print(f"[i] Snapshot {number} doesn't exist")
        continue
