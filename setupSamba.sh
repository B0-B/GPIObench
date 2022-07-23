#!/usr/bin/env bash

# This script will install samba and install a user "pi".
# A password needs to be set, and the pi can be added to windows filesystem

sudo apt install -y samba &&
echo "\n[PiShare]\n comment=Pi Share\n path=/home/pi\n browseable=yes\n writeable=yes\n only guest=no\n create mask=0740\n directory mask=0750\n public=no" >> sudo nano /etc/samba/smb.conf &&
sudo smbpasswd -a pi