[PT/EN]

 	   ____                  _ _          _             
	  / ___|__ _ _ __   __ _(_) |__  _ __(_)_ __   __ _ 
	 | |   / _` | '_ \ / _` | | '_ \| '__| | '_ \ / _` |
	 | |__| (_| | | | | (_| | | |_) | |  | | | | | (_| |
	  \____\__,_|_| |_|\__, |_|_.__/|_|  |_|_| |_|\__,_|
		               |___/                Beta - v0.8.7
	  Dashboard Finder


	  Cangibrina 0.8.5 | coded by Fnkoc

====================================================================================================

Dashboard Finder 

Cangibrina is a multi platform tool which aims to obtain the Dashboard of sites using brute-force 
over wordlist, google, nmap, and robots.txt

Requirements:  
====================================================================================================
* Python 2.7    
* mechanize  
* PySocks  
* beautifulsoup4  
* html5lib  
* Nmap (--nmap)  
* TOR (--tor)  

Install:         
====================================================================================================     
**Linux**  
```
	git clone http://github.com/fnk0c/cangibrina.git
	cd cangibrina
	pip install -r requeriments.txt
```

[English Version]

```
usage: cangibrina.py [-h] -u U [-w W] [-t T] [-v] [--ext EXT] [--user-agent]
                     [--tor] [--search] [--dork DORK] [--nmap [NMAP]]

Fast and powerful admin finder

optional arguments:
  -h, --help     show this help message and exit
  -u U           target site
  -w W           set wordlist (default: wl_medium)
  -t T           set threads number (default: 5)
  -v             enable verbose
  --ext EXT      filter path by target extension
  --user-agent   modify user-agent
  --tor          set TOR proxy
  --search       use google and duckduckgo to search
  --dork DORK    set custom dork
  --nmap [NMAP]  use nmap to scan ports and services

```

===============================================================================

```
	Examples:

	python cangibrina.py -u facebook.com

	python cangibrina.py -u facebook.com -v

	python cangibrina.py -u facebook.com -w /root/diretorios.txt -t 10 -v

	python cangibrina.py -u facebook.com --search -v

	python cangibrina.py -u facebook.com --search --dork 'site:facebook.com inurl:login'

	python cangibrina.py -u facebook.com -v --nmap

	python cangibrina.py -u facebook.com -v --nmap 'sudo nmap -D 127.0.0.1 -F facebook.com'

	python cangibrina.py -u facebook.com --user-agent

	python cangibrina.py -u facebook.com --ext php

		[IMPORTANT] DORK MUST BE WRITE BETWEEN QUOTES !
		[Example] 'inurl:login.php'
```
