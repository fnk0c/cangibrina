#!/usr/bin/python
#coding=utf-8

__AUTOR__	= "Fnkoc"
__DATA__	= "19/12/14"
__VERSAO__	= "0.8.3"

'''Agradecimento especial ao Maximoz'''

import sys
sys.path.append("src/")
import Connection
import colors
import argparse
import os
import time
import Nmap
import search
import threading
from threading import Thread


'''==============================================================================='''
def ajuda():

	import Clear

	print("""   ____                  _ _          _             
  / ___|__ _ _ __   __ _(_) |__  _ __(_)_ __   __ _ 
 | |   / _` | '_ \ / _` | | '_ \| '__| | '_ \ / _` |
 | |__| (_| | | | | (_| | | |_) | |  | | | | | (_| |
  \____\__,_|_| |_|\__, |_|_.__/|_|  |_|_| |_|\__,_|
                   |___/              Beta - v0.8.3
  Dashboard Finder

  Cangibrina 0.8.3 | coded by Fnkoc

usage: cangibrina.py -u[URL] -w[WORDLIST] -t[THREADS] -g -d[DORK] -s[OUTPUT] -p[PROXY] -v -n -a

Arguments:

  -h\t--help\t\tShow this help and exit
  -u\t--url\t\tDefine target site
  -w\t--wordlist\tDefine wordlist (optional)
  -v\t--verbose\tEnable verbose mode
  -t\t--threads\tTells the number of process to be used
\t\t\t(optional, default = 7)
  -g\t--google\tSearch through Google e DuckDuckGo engine
  -d\t--dork\t\tSearch dork to use
  -s\t--saida\t\tOutput name to be use
  -n\t--nmap\t\tUses Nmap to check for ports and services
  -a\t--user_agent\tChange User-Agent
  -p\t--proxy\t\tUse proxy server (ONLY HTTP)
    \t--update\tUpdate tool

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
""")
	print(colors.red + "[IMPORTANT] DORK MUST BE WRITE BETWEEN QUOTES !\n"+ colors.default)
	print(colors.red + "[Example] 'inurl:login.php'\n\n" + colors.default)


'''====A.R.G.U.M.E.N.T.O.S========================================================'''

parser = argparse.ArgumentParser(description = "Cangibrina", add_help = False)
parser.add_argument("-h", "--help", action = "store_true",
				help = "Mostra esta ajuda e sai")
parser.add_argument("-u", "--url",
				help = "Informa site alvo")
parser.add_argument("-w", "--wordlist",
				help = "Informa wordlist a ser usada")
parser.add_argument("-v", "--verbose",
				action = "store_true", help = "Habilita modo verbose")
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
#parser.add_argument("--tor", action = "store_true",
#				help = "Usa tor para proxy")

args = parser.parse_args()

"""====F.U.N.C.O.E.S=========================================================="""

"""====W.O.R.D.L.I.S.T========================================================"""

def read_wl(wordlist):

	def create_lst():
		global lst
		lst = []

		for i in diretorios:
			lst.append(i)
	try:
		if wordlist == None:		#Caso seja específicada uma wordlist
			os.chdir("Wordlists")	#Caso NÃO sejá especificada uma wordlist será usada a padrão
			diretorios = open("default", "r").readlines()
			create_lst()
			
		else:
			diretorios = open(wordlist, "r").readlines()
			create_lst()
			
	except Exception, e:
		print colors.red + " [!] " + colors.default + str(e) + "\n"
		sys.exit()

"""====B.R.U.T.E.-.F.O.R.C.E=================================================="""

def brute_force(lst):
	for ways in lst:
		final = url + ways
		lst.remove(ways)
		Connection.tester(final, proxy, user_agent, verbose, saida)

		if verbose:
			print final
		else:
			pass
	
	sys.exit()

"""====P.L.U.S================================================================"""
	
def plus():
	print colors.green + " [+] " + colors.default + "Checking for Robots.txt"
	robots = url + "robots.txt"	
	print robots
	Connection.tester(robots, proxy, user_agent, verbose, saida)

	os.system("pwd")
	os.chdir("..")
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

	"""====R.E.S.U.L.T========================================================"""
	print colors.red + "\n" + ("-"*80) + colors.default
	print colors.green + " [+] " + colors.default + "[Results]\n"
	Connection.result()
	print colors.red + ("-"*80) + "\n" + colors.default
	
	sys.exit()

"""====M.A.I.N================================================================"""

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
	dork = args.dork
	nmap = args.nmap
	update = args.update
#	tor = args.tor

	"""====A.R.R.U.M.A.-.U.R.L================================================"""
	
	if update:
		os.system("git fetch && git pull")
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
	
	Connection.redirect_tester(url, proxy, user_agent, verbose)
	read_wl(wordlist)
	print colors.green + "\n [+] " + colors.default + "Testing..."

	if __name__ == "__main__":
		for t in range(args.threads):							  # For se refere ao número de processos que será criado
			Thread(target = (brute_force), args = (lst,)).start() #A segunda virgula é para transformar os args em tupla
			time.sleep(1.2)										  # Caso não coloque o sleep os processos irão se sobrepor
						
		while 1==1:								#Durante a execução do programa é checado o número de threads
			if threading.active_count() == 1:	#sendo executados. Quando for igual a um significa que o brute force 
				plus()							#já foi concluido, podendo assim seguir para as proximas etapas
			elif threading.active_count() > 1:
				pass
