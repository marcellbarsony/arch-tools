#!/usr/bin/env python3
"""
Remove orphaned Snapper snapshots
"""

import subprocess

for number in range(1, 1000):
    try:
        path = f"/home/.snapshots/{number}/snapshot"
        cmd = f"sudo btrfs subvolume delete {path}"
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except Exception:
        print(f":: [i] :: Snapshot {number} doesn't exist")
        continue
    else:
        print(f":: [+] :: Removing snapshot {number} - {path}")
