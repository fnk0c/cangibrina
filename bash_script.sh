#/bin/bash

touch /usr/bin/cangibrina
echo \#/bin/bash >> /usr/bin/cangibrina
echo cd /home/franco/Documentos/programação/Projetos/Cangibrina/cangibrina/ >> /usr/bin/cangibrina
echo exec python2 cangibrina-1.7.py \"\$\@\" >> /usr/bin/cangibrina
chmod +x /usr/bin/cangibrina