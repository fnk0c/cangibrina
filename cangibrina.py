#!/usr/bin/python
#coding=utf-8

__AUTOR__	= "Fnkoc"
__DATA__	= "19/06/15"
__VERSAO__	= "0.8.6"
__GITHUB__	= "https://github.com/fnk0c"

'''Agradecimento especial ao Maximoz e BernardoGO'''

"""
    Copyright (C) 2015  Franco Colombino

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

import sys
sys.path.append("src/")
import argparse
import os
import threading
import Connection
import colors
import Nmap
import search
from time import sleep
from threading import Thread

"""=========================================================================="""
def ajuda():

	import Clear

	print("""%s   ____                  _ _          _             
  / ___|__ _ _ __   __ _(_) |__  _ __(_)_ __   __ _ 
 | |   / _` | '_ \ / _` | | '_ \| '__| | '_ \ / _` |
 | |__| (_| | | | | (_| | | |_) | |  | | | | | (_| |
  \____\__,_|_| |_|\__, |_|_.__/|_|  |_|_| |_|\__,_|
                   |___/%s              Beta - v%s
  %sDashboard Finder%s

  Cangibrina %s | coded by Fnkoc

usage: cangibrina.py -u[URL] -w[WORDLIST] -t[THREADS] -g -d[DORK] -s[OUTPUT] \
-p[PROXY] --ext[EXT] -T -v -n -a 

Arguments:

  -h\t--help\t\tShow this help and exit
  -u\t--url\t\tDefine target site (required)
  -w\t--wordlist\tDefine wordlist (optional)
  -v\t--verbose\tEnable verbose mode
  -T\t--tor\t\tEnable TOR mode
  -t\t--threads\tTells the number of process to be used (default = 7)
  -g\t--google\tSearch through Google e DuckDuckGo engine
  -d\t--dork\t\tSearch dork to use
  -s\t--saida\t\tOutput name to be use
  -n\t--nmap\t\tUses Nmap to check for ports and services
  -a\t--user_agent\tChange User-Agent
  -p\t--proxy\t\tUse proxy server (ONLY HTTP)
    \t--update\tUpdate tool
    \t--ext\t\tDefine page extension (asp, aspx, php, brf, cfm, cgi, js, php)

================================================================================

Examples:

python cangibrina.py -u facebook.com

python cangibrina.py -u facebook.com -v -s facebook

python cangibrina.py -u facebook.com -w /root/diretorios.txt -t 10 -v

python cangibrina.py -u facebook.com -g -v

python cangibrina.py -u facebook.com -g -d 'site:facebook.com inurl:login' -s \
face

python cangibrina.py -u facebook.com -v -n

python cangibrina.py -u facebook.com -a

python cangibrina.py -u facebook.com -p 187.25.2.485:8080

python cangibrina.py -u facebook.com -T

python cangibrina.py -u facebook.com --ext php
""" % (colors.white, colors.default, __VERSAO__, colors.red, colors.default,\
__VERSAO__))
	print(colors.red + "[IMPORTANT] DORK MUST BE WRITE BETWEEN QUOTES !\n"+ \
colors.default)
	print(colors.red + "[Example] 'inurl:login.php'\n\n" + colors.default)


"""====A.R.G.U.M.E.N.T.O.S==================================================="""

parser = argparse.ArgumentParser(description = "Cangibrina", add_help = False)
parser.add_argument("-h", "--help", action = "store_true",
		help = "Mostra esta ajuda e sai")
parser.add_argument("-u", "--url",
		help = "Informa site alvo")
parser.add_argument("-w", "--wordlist",
		help = "Informa wordlist a ser usada")
parser.add_argument("-v", "--verbose",
		action = "store_true", help = "Habilita modo verbose")
parser.add_argument("-T", "--tor",
		action = "store_true", help = "Habilita TOR")
parser.add_argument("-t", "--threads",default = 7, type = int,
		help = "Informa número de processos a serem executados\n Default=10")
parser.add_argument("-g", "--google", 
		action = "store_true", help = "Busca de sites")
parser.add_argument("-d", "--dork",
		nargs = "+", help = "Dork de Busca")
parser.add_argument("-s", "--saida",
		default = "log_busca", help = "Informa nome do arquivo log")
parser.add_argument("-n", "--nmap",
		action = "store_true", help = "nmap")
parser.add_argument("-a", "--user_agent",
		action = "store_true", help = "Habilita user agent")
parser.add_argument("-p", "--proxy",
		help = "Utiliza servidor proxy")
parser.add_argument("--update",
		action = "store_true", help = "Faz Update da tool")
parser.add_argument("--ext",
		nargs = 1, help="Define extensao pagina")

args = parser.parse_args()

"""====F.U.N.C.O.E.S========================================================="""

"""====W.O.R.D.L.I.S.T======================================================="""

def read_wl(wordlist):

	def create_lst():
		global lst
		lst = []

		for i in diretorios:
			lst.append(i)
	try:
		if wordlist == None:		#Caso seja específicada uma wordlist
			os.chdir("Wordlists")	#Caso NÃO sejá especificada uma wordlist será usada a padrão
			diretorios = open("wl_default", "r").readlines()
			os.chdir("..")
			create_lst()
			
		else:
			diretorios = open(wordlist, "r").readlines()
			create_lst()
			
	except Exception as e:
		print (colors.red + " [!] " + colors.default + str(e) + "\n")
		sys.exit()

"""====B.R.U.T.E.-.F.O.R.C.E================================================="""
def renew_tor():
	import socket

	s = socket.socket()
	s.connect(('localhost', 9050))

	s.send('AUTHENTICATE "{0}"\r\n'.format("123"))
	resp = s.recv(1024)

	if resp.startswith('250'):
		s.send("signal NEWNYM\r\n")

		resp = s.recv(1024)

		if resp.startswith('250'):
			print ("TOR Identity Renewed")
		else:
			print ("response 2: "+resp)
	else:
		print ("response 1: "+resp)



def brute_force(lst):
	def process():
		final = url + ways
		lst.remove(ways)
		
		Connection.tester(final, proxy, user_agent, verbose, saida)

		if verbose:
			print (final)
		else:
			pass

	for ways in lst:
		if ext:
			if "." in ways:
				ex = "".join(ext)
				if ex in ways:
					process()
				else:
					pass
			else:
				process()
		else:
			process()	
	sys.exit()

"""====P.L.U.S==============================================================="""
	
def plus():
	print (colors.green + " [+] " + colors.default + "Checking for Robots.txt")
	robots = url + "robots.txt"	
	print (robots)
	Connection.tester(robots, proxy, user_agent, verbose, saida)

	os.chdir("output")
	if google:
		search.google(dork, saida, url)
		search.DuckDuckGo(dork, saida, url)
	else:
		pass

	if nmap:
		Nmap.run(url)
	else:
		pass

	"""====R.E.S.U.L.T======================================================="""
	print (colors.red + "\n" + ("-"*80) + colors.default)
	print (colors.green + " [+] " + colors.default + "[Results]\n")
	Connection.result()
	print (colors.red + ("-"*80) + "\n" + colors.default)
	
	sys.exit()

"""====M.A.I.N==============================================================="""

if len(sys.argv) == 1:
	ajuda()

else:
	url = args.url
	proxy = args.proxy
	user_agent = args.user_agent
	saida = args.saida
	threads = args.threads
	verbose = args.verbose
	wordlist = args.wordlist
	google = args.google
	tor = args.tor
	dork = args.dork
	nmap = args.nmap
	update = args.update
	ext = args.ext
	help = args.help

	"""====A.R.R.U.M.A.-.U.R.L==============================================="""
	
	if update:
		os.system("git fetch && git pull")
		sys.exit()

	elif help == True:
		ajuda()
		sys.exit()

	else:
		pass

	if url[:11] == "http://www.":
		url = url[11:]
	elif url[:4] == "www.":
		url = url[4:]
	elif url[:7] == "http://":
		url = url[7:]
	
	url = "http://www.%s/" % url
	
	if tor == True:
		try:
			renew_tor()
			import socks
			import socket
			import mechanize
			from mechanize import Browser

			def create_connection(address, timeout=None, source_address=None):
				sock = socks.socksocket()
				sock.connect(address)
				return sock

			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

			# patch the socket module
			socket.socket = socks.socksocket
			socket.create_connection = create_connection

			br = Browser()
			print ("New Identity: " + br.open('http://icanhazip.com').read())

		except Exception as e:
			print(colors.red + " [-] " + colors.default + str(e))
			print(colors.yellow + " [!] " + colors.default + "Check if TOR is \
running on 127.0.0.1:9050")
			sys.exit()

	Connection.redirect_tester(url, proxy, user_agent, verbose)
	read_wl(wordlist)
	print (colors.green + "\n [+] " + colors.default + "Testing...")

	if __name__ == "__main__":
		for t in range(args.threads):							  # For se refere ao número de processos que será criado
			Thread(target = (brute_force), args = (lst,)).start() #A segunda virgula é para transformar os args em tupla
			sleep(1.2)											  # Caso não coloque o sleep os processos irão se sobrepor
						
		while 1==1:								#Durante a execução do programa é checado o número de threads
			if threading.active_count() == 1:	#sendo executados. Quando for igual a um significa que o brute force 
				plus()							#já foi concluido, podendo assim seguir para as proximas etapas
			elif threading.active_count() > 1:
				pass
