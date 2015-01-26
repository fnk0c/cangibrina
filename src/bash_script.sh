#/bin/bash

if [ -e /usr/bin/cangibrina ]
then
	rm /usr/bin/cangibrina
	echo limpando arquivos obsoletos
fi

cd ..
cd ..
if [ -e //opt/cangibrina ]
then
	rm -r /opt/cangibrina
	echo limpando arquivos obsoletos
fi

mv cangibrina /opt/
touch /usr/bin/cangibrina
echo \#/bin/bash >> /usr/bin/cangibrina
echo cd /opt/cangibrina >> /usr/bin/cangibrina
echo exec python2 cangibrina.py \"\$\@\" >> /usr/bin/cangibrina
chmod +x /usr/bin/cangibrina
echo Processo finalizado.
echo cangibrina disponivel em /opt/cangibrina ou digitando cangibrina em seu terminal
