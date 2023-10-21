#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : 20 October 2023
Desc  : DNS tools
"""


# Flush cache
systemd_resolve = "sudo systemd-resolve --flush-caches"
resolvectl = "sudo resolvectl flush-caches"
firefox = "about:networking#dns"
chrome = "chrome://net-internals/#dns"

# Resolvconf
# https://wiki.archlinux.org/title/Openresolv
resolvconf = "/etc/resolvconf.conf"
conf_gen = "resolvconf -u"
conf_file = "/etc/resolv.conf"
# https://wiki.archlinux.org/title/Domain_name_resolution#Overwriting_of_/etc/resolv.conf
# To prevent programs from overwriting /etc/resolv.conf, it is also possible to write-protect it by setting the immutable file attribute:
chattr +i /etc/resolv.conf

# systemd-resolved
# https://wiki.archlinux.org/title/systemd-resolved
# https://wiki.archlinux.org/title/NetworkManager#systemd-resolved
# https://wiki.archlinux.org/title/NetworkManager#Use_openresolv
systemd_resolved_service = "sudo systemctl start systemd-resolved.service"
systemd_resolved_conf = "sudoedit /etc/systemd/resolved.conf"
systemd_resolved_status = "resolvectl status"
