#!/bin/bash
apt-get update
apt full-upgrade -y
apt autoremove -y
timedatectl set-timezone Asia/Tokyo
echo 'ubuntu ALL=NOPASSWD: ALL' | EDITOR='tee -a' visudo
ufw allow 22
ufw enable
chmod 700 ssh_setting.sh && ./ssh_setting.sh
adduser -q --gecos "" --disabled-login ubuntu
gpasswd -a ubuntu sudo
