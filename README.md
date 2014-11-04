  ____                  _ _          _             
 / ___|__ _ _ __   __ _(_) |__  _ __(_)_ __   __ _ 
| |   / _` | '_ \ / _` | | '_ \| '__| | '_ \ / _` |
| |__| (_| | | | | (_| | | |_) | |  | | | | | (_| |
 \____\__,_|_| |_|\__, |_|_.__/|_|  |_|_| |_|\__,_|
                  |___/               Beta - v0.8.1
 Dashboard Finder

 Cangibrina 0.8.1 | coded by Fnkoc
	  
====================================================================================================

Dashboard Finder 
 
Cangibrina é uma ferramenta multiplataforma que visa a obtenção do painel de administração de sites 
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

Instalação Linux:
====================================================================================================     
Faça o download do programa, entre no diretório e execute o script "linux_install.sh"

	git clone http://github.com/fnk0c/cangibrina.git
	cd cangibrina
	sh linux_install.sh

Uso/Ajuda:
====================================================================================================     
	uso: cangibrina-0.8.py -u[url] -w[wordlist] -t[threads] -g -d[DORK] -s[SAIDA] -v -n -a

	Comandos:

	  -h	--help\t\tExibe esta ajuda e sai
	  -u	--url\t\tDefine site alvo
	  -w	--wordlist\tDefine wordlist (opcional)
	  -v	--verbose\tHabilita modo verbose
	  -t	--threads\tInforma número de processos a serem executados (opcional, default = 10)
	  -g	--google\tBusca através dos motores Google e DuckDuckGo
	  -d	--dork\t\tInforma dork de busca
	  -s	--saida\t\tInforma nome do arquivo log gerado
	  -n	--nmap\t\tUtliza o Nmap para scan de serviços
	  -a	--user_agent\tAdiciona user-agent

	===============================================================================

	Exemplos de uso:

	python cangibrina.py -u facebook.com -w /root/diretorios.txt -t 10 -v
	Foi utilizada uma wordlist personalizada, 10 threads, o modo verbose e o facebook.com como alvo

	python cangibrina.py -u facebook.com -v -s face_brute
	Foi utilizada a wordlist e threads padrões. facebook.com como alvo, modo verbose e arquivo log gerado receberá o nome face_brute

	python cangibrina.py -u facebook.com -g -s face -v
	Foi utilizada a busca do painel através de requests e dos motores de busca, gerando um arquivo "face" com os resultados

	python cangibrina.py -u facebook.com -g -d 'inurl:login' -s face
	Foi utilizado o facebook.com como alvo, wordlist e threads padrões, motores de busca, e dork personalizada.

	python cangibrina.py -u facebook.com -v -n -a
	Foi utilizado o facebook.com como alvo, wordlist e threads padrões, verbose, user-agent e nmap para scan de portas.

	[IMPORTANTE] DORK DEVE SER ESCRITA ENTRE ASPAS SIMPLES!
     

====================================================================================================
Bugs Conhecidos: 
Primeira execução costuma utilizar apenas um thread. Caso aconteça, basta fechar o terminal e
reiniciar a execução do Cangibrina.
