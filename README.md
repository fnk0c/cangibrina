cangibrina
==========

Dashboard Finder 
 
Cangibrina é uma ferramenta que visa a obtenção do painel de administração de sites 
utilizando requests, google, nmap e uma wordlist para isso. 

Requisitos:  
====================================================================================================
Python 2.7    
mechanize    
Nmap para o argumento -n    

====================================================================================================
Como instalar Mechanize:     
Linux:     
        Debian: sudo apt-get install python-mechanize     
        Arch: sudo pacman -S python2-mechanize     
Windows:       
        Download: https://pypi.python.org/pypi/mechanize/     
        python setup.py install     

Instalação:
====================================================================================================     
Faça o download do programa

	git clone http://github.com/fnk0c/cangibrina.git

como root rode o script "bash_script.sh"

	sudo sh bash_script.sh

Uso:
====================================================================================================     
cangibrina -u target.com -w /root/wordlist.txt -t 15 -v -g -d 'inurl:login' -s target_out -n 

-u > referente ao site alvo  
-w > referente a wordlist personalizada  
-t > referente ao número de processos (threads) criados  
-v > referente ao modo verbose  
-g > referente a busca do google  
-d > referente a dork (entre aspas simples)  
-s > referente ao arquivo gerado com os resultados do google  
-n > referente ao uso do nmap para scannear portas no servidor  

Outros exemplos:      
cangibrina -u facebook.com -w /root/diretorios.txt -t 10 -v  
cangibrina -u facebook.com -v  
cangibrina -u facebook.com -g -s face -v  
cangibrina -u facebook.com -g -d 'inurl:login' -s face  
cangibrina -u facebook.com -g -d 'inurl:login' -s face -n  
 
====================================================================================================
Bugs Conhecidos: 
Primeira execução costuma utilizar apenas um thread. Caso aconteça, basta fechar o terminal e
reiniciar a execução do Cangibrina.
