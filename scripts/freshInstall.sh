#!/bin/bash


echo Installing standard software

# Change to root user
su

apt update
apt upgrade

apt install zsh
apt install git
apt install node
apt install npm
apt install python3
apt install rsync
apt install htop
apt install gdebi-core


echo Configuring zsh
# Configuring zsh
chsh -s /bin/zsh
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"


echo Setting global git config
# Set up github configuration
git config --global user.name "jrtechs"
git config --global user.email "jeffery@jrtechs.net"



echo Installing bash manager
cd /home/jeff

mkdir media
mkdir public
mkdir work

mkdir scripts
cd scripts
git clone https://github.com/jrtechs/bash_manager.git


echo Enabling non-root users to mount ssh drives
# Enables non-root users to mount ssh drives
echo "user_allow_other" >> /etc/fuse.conf


echo Installing all the fun software with snap.
# On Work Stations
apt install snapd

## Discord
snap install discord

## Slack
snap install slack --classic

snap install spotify

snap install obs-studio

snap install vscode --classic

snap install vlc

snap install chromium


## JetBrains Stuff
snap install pycharm-professional --classic
snap install intellij-idea-community --classic
snap install phpstorm --classic
snap install webstorm --classic

echo Restart!!

reboot










