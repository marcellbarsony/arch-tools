#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : July 2023
Desc  : OpenVPN setup
"""


import subprocess
import sys


class OpenVPN():

    """
    Docstring for OpenVPN
    https://wiki.archlinux.org/title/OpenVPN
    """

    @staticmethod
    def openvpn_install():
        cmd = "sudo pacman -S --noconfirm openvpn"
        # [TODO]: Remove redundant installations
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] OpenVPN install")
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def openvpn_config():
        """https://wiki.archlinux.org/title/OpenVPN#The_client_configuration_profile"""
        cmd = "sudo cp /usr/share/openvpn/examples/client.conf /etc/openvpn/client/"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] OpenVPN config")
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def openvpn_reolved(arg):
        cmd = "pikaur -S --noconfirm openvpn-update-systemd-resolved"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)


class ProtonVPN():

    """
    Docstring for ProtonVPN
    https://protonvpn.com/support/linux-openvpn/
    """

    @staticmethod
    def cfg_get():
        cmd = "sudo wget https://raw.githubusercontent.com/ProtonVPN/scripts/master/update-resolv-conf.sh -O /etc/openvpn/update-resolv-conf"

    @staticmethod
    def cfg_chmod():
        cmd = "sudo chmod +x /etc/openvpn/update-resolv-conf"

if __name__ == "__main__":
    o = OpenVPN()
    o.openvpn_install()
    o.openvpn_config()

    p = ProtonVPN()
    p.cfg_get()
    p.cfg_chmod()

