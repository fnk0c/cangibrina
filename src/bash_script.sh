#!/bin/bash

if [ -e /usr/bin/cangibrina ]
then
	rm /usr/bin/cangibrina
fi

cd .. && cd ..

if [ -e /opt/cangibrina ]
then
	rm -r /opt/cangibrina
	echo limpando arquivos obsoletos
fi

echo \#\!/bin/bash >> /usr/bin/cangibrina
echo cd /opt/cangibrina >> /usr/bin/cangibrina
echo exec python2 cangibrina.py \"\$\@\" >> /usr/bin/cangibrina

mv cangibrina /opt/
chmod +x /usr/bin/cangibrina

echo ' [+] Pronto | Ready' .
echo 'cangibrina disponivel em /opt/cangibrina ou digitando cangibrina em seu terminal'
echo 'Cangibrina is available at /opt/cangibrina or typing cangibrina on your terminal'
