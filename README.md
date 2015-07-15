[PT/EN]

 	   ____                  _ _          _             
	  / ___|__ _ _ __   __ _(_) |__  _ __(_)_ __   __ _ 
	 | |   / _` | '_ \ / _` | | '_ \| '__| | '_ \ / _` |
	 | |__| (_| | | | | (_| | | |_) | |  | | | | | (_| |
	  \____\__,_|_| |_|\__, |_|_.__/|_|  |_|_| |_|\__,_|
		               |___/                Beta - v0.8.5
	  Dashboard Finder


	  Cangibrina 0.8.5 | coded by Fnkoc

====================================================================================================

Dashboard Finder 

Cangibrina é uma ferramenta multiplataforma que visa a obtenção do painel de administração de sites 
utilizando brute-force baseado e wordlist, google, nmap e robots.txt.

Cangibrina is a multi platform tool which aims to obtain the Dashboard of sites using brute-force 
over wordlist, google, nmap, and robots.txt

Requisitos/Requirements:  
====================================================================================================
Python 2.7    
mechanize    
beautifulsoup  
Nmap para o argumento -n    /	Nmap to use argument -n        
python-socksipy socks to use argument -T (TOR)      

Instalação/ Install:         
====================================================================================================     
**Linux**  
Faça o download do programa, entre no diretório e execute o script "setup.py"

Do the download, enter the directory and run the script "setup.py"

	git clone http://github.com/fnk0c/cangibrina.git
	cd cangibrina
	python setup.py install

**Windows**  
Faça o download do programa, extraia, entre no diretório e execute o script "setup.py"  

Do the download, extract, enter the directory and run the script "setup.py"  

	https://github.com/fnk0c/cangibrina/archive/master.zip
	python setup.py install


===========
## Se prefere fazer manualmete. Siga as etapas: 
## If you prefer to install manually. Follow the steps:  

####Como instalar Mechanize/How to install Mechanize:     
######Linux:  
	Debian: sudo apt-get install python-mechanize  
	Arch: sudo pacman -S python2-mechanize  
######Windows:  
	Download: https://pypi.python.org/pypi/mechanize/          
	python setup.py install         

####Como instalar python-socksipy/How to install python-socksipy:           
######Linux:     
	Debian: sudo apt-get install python-socksipy (OPTIONAL FOR TOR)       
	Arch: sudo pacman -S python2-socks         

####Como instalar BeautifulSoup/How to install BeautifulSoup:     
######Linux:      
	Debian: sudo apt-get install python-beautifulsoup       
	Arch: sudo pacman -S python2-beautifulsoup4     
######Windows:
	Download: https://pypi.python.org/pypi/beautifulsoup4  
	python setup.py install  

Video Tutorial
====================================================================================================     
https://www.youtube.com/watch?v=XEOjA3DUTNA

Ajuda/help:
====================================================================================================     
[Versão em Português]

	uso: cangibrina.py -u[url] -w[wordlist] -t[threads] -g -d[DORK] -s[SAIDA] -p[PROXY] --ext[EXT] -T -v -n -a

	Comandos:

	  -h	--help			Exibe esta ajuda e sai
	  -u	--url			Define site alvo
	  -w	--wordlist		Define wordlist (opcional)
	  -v	--verbose		Habilita modo verbose
	  -T	--tor			Utiliza TOR como proxy
	  -t	--threads		Informa número de processos a serem executados (opcional, default = 10)
	  -g	--google		Busca através dos motores Google e DuckDuckGo
	  -d	--dork			Informa dork de busca
	  -s	--saida			Informa nome do arquivo log gerado
	  -n	--nmap			Utliza o Nmap para scan de serviços
	  -a	--user_agent	Adiciona user-agent
	  -p	--proxy			Utiliza servidor proxy (Apenas HTTP)
	    	--update		Atualiza ferramenta
	    	--ext			Define extensao da página (asp, aspx, php, brf, cfm, cgi, html, js, php)


	===============================================================================

	Exemplos de uso:

	python cangibrina.py -u facebook.com

	python cangibrina.py -u facebook.com -v -s facebook

	python cangibrina.py -u facebook.com -w /root/diretorios.txt -t 10 -v

	python cangibrina.py -u facebook.com -g -v

	python cangibrina.py -u facebook.com -g -d 'site:facebook.com inurl:login' -s face

	python cangibrina.py -u facebook.com -v -n

	python cangibrina.py -u facebook.com -a

	python cangibrina.py -u facebook.com -p 187.25.2.485:8080
	
	python cangibrina.py -u facebook.com --ext php

		[IMPORTANTE] DORK DEVE SER ESCRITA ENTRE ASPAS SIMPLES!
		[Example] 'inurl:login.php'
 
 
[English Version]

	usage: cangibrina.py -u[URL] -w[WORDLIST] -t[THREADS] -g -d[DORK] -s[OUTPUT] -p[PROXY] --ext[EXT] -T -v -n -a

	Arguments:

	  -h 	--help			Show this help and exit
	  -u	--url			Define target site
	  -w	--wordlist		Define wordlist (optional)
	  -v	--verbose		Enable verbose mode
      -T	--tor			Use TOR as proxy
	  -t	--threads		Tells the number of process to be used (optional, default = 7)
	  -g	--google		Search through Google e DuckDuckGo engine
	  -d	--dork			Search dork to use
	  -s	--saida			Output name to be use
	  -n	--nmap			Uses Nmap to check for ports and services
	  -a 	--user_agent	Change User-Agent
	  -p	--proxy			Use proxy server (ONLY HTTP)
  	    	--update		Update tool
	    	--ext			Define page extension (asp, aspx, php, brf, cfm, cgi, html, js, php)


	===============================================================================

	Examples:

	python cangibrina.py -u facebook.com

	python cangibrina.py -u facebook.com -v -s facebook

	python cangibrina.py -u facebook.com -w /root/diretorios.txt -t 10 -v

	python cangibrina.py -u facebook.com -g -v

	python cangibrina.py -u facebook.com -g -d 'site:facebook.com inurl:login' -s face

	python cangibrina.py -u facebook.com -v -n

	python cangibrina.py -u facebook.com -a

	python cangibrina.py -u facebook.com -p 187.25.2.485:8080
	
	python cangibrina.py -u facebook.com --ext php

		[IMPORTANT] DORK MUST BE WRITE BETWEEN QUOTES !
		[Example] 'inurl:login.php'

Gerando Wordlists/ Generating Wordlists
=======================================
[Versão em Português]  

Você pode gerar wordlists customizadas através da ferramenta wlgenerator.py localizada em  
Wordlists/wl generator/  
Dentro do diretório você encontrará 3 arquivos de texto, diretorios, extensoes, paginas. Estes  
são responsáveis por conter as informações necessárias para a geração da wordlist.  

[English Version]  

You can generate customs wordlists using the tool wlgenerator.py located at Wordlists/wl generator  
Inside this directory you will find 3 text files, diretorios, extensoes, paginas. These are  
responsible to keep all the necessary informations that are required to generate a wordlist  

Bugs: 
====================================================================================================
Se achar algum bug, favor me avisar:  
If you found any bug, please notify me:  

franco.c.colombino@gmail.com  
fb.com/fnkoc.a  
