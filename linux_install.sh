#!/bin/bash

#Check user privilege
if [ "$(id -u)" != "0" ]; then
	clear
	echo "This script must be run as root" 1>&2
	exit
fi
#end check

#Check for exiting files
if [ -e /usr/bin/cangibrina ]
then
	rm /usr/bin/cangibrina
fi

cd ..

if [ -e /opt/cangibrina ]
then
	rm -r /opt/cangibrina
	echo limpando arquivos obsoletos
fi
#end check

#create symbolic links
echo \#\!/bin/bash >> /usr/bin/cangibrina
echo cd /opt/cangibrina >> /usr/bin/cangibrina
echo exec python2 cangibrina.py \"\$\@\" >> /usr/bin/cangibrina
#end links

#move tool
mv cangibrina /opt/
chmod +x /usr/bin/cangibrina
#end move

#Check distro
if [ -e /etc/apt ]
then
	apt-get install python-mechanize python-socksipy python-bs4
fi

if [ -e /etc/pacman.d ]
then
	pacman -S python2-mechanize python2-socks python2-beautifulsoup4
fi

echo ' [+] Pronto | Ready' .
echo 'cangibrina disponivel em /opt/cangibrina ou digitando cangibrina em seu terminal'
echo 'Cangibrina is available at /opt/cangibrina or typing cangibrina on your terminal'
