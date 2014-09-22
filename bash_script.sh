#/bin/bash

cd ..
mv cangibrina /opt/
touch /usr/bin/cangibrina
echo \#/bin/bash >> /usr/bin/cangibrina
echo cd /opt/cangibrina >> /usr/bin/cangibrina
echo exec python2 cangibrina-1.7.py \"\$\@\" >> /usr/bin/cangibrina
chmod +x /usr/bin/cangibrina
echo Processo finalizado.
echo cangibrina disponivel em /opt/cangibrina ou digitando cangibrina em seu terminal