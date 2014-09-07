cangibrina
==========

Dashboard Finder 
 
Cangibrina é uma ferramenta que visa a obtenção do painel de administração de sites 
utilizando requests, google, nmap e uma wordlist para isso. 

====================================================================================================
Requisitos:       
Python 2.7    
mechanize    
Nmap para o argumento -n    

====================================================================================================
Como instalar Mechanize:     
Linux:     
	Debian: sudo apt-get install python-mechanize     
	Arch: sudo pacman -S python2-mechanize      

====================================================================================================
Uso:     
python cangibrina-1.7.py -u target.com -w /root/wordlist.txt -t 15 -v -g -d 'inurl:login' -s target

-u > referente ao site alvo  
-w > referente a wordlist personalizada  
-t > referente ao número de processos (threads) criados  
-v > referente ao modo verbose  
-g > referente a busca do google  
-d > referente a dork (entre aspas simples)  
-s > referente ao arquivo gerado com os resultados do google  
-n > referente ao uso do nmap para scannear portas no servidor  

Outros exemplos:      
python cangibrina-1.7.py -u facebook.com -w /root/diretorios.txt -t 10 -v  
python cangibrina-1.7.py -u facebook.com -v  
python cangibrina-1.7.py -u facebook.com -g -s face -v  
python cangibrina-1.7.py -u facebook.com -g -d 'inurl:login' -s face  
python cangibrina-1.7.py -u facebook.com -g -d 'inurl:login' -s face -n  
 
====================================================================================================
Bugs Conhecidos: 
Primeira execução costuma utilizar apenas um thread, caso aconteça basta fechar o terminal e
reiniciar a execução do Cangibrina 
