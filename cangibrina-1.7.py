#!/usr/bin/python
#coding=utf-8


__AUTOR__	= 'Fnkoc'
__DATA__	= '31/08/14'
__VERSAO__	= '1.7'

'''Agradecimento especial ao Maximoz'''

import sys
sys.path.append('src/thirdparty/beautifulsoup4-4.3.2/')		#Adiciona diretório para busca de bibliotecas/modulos
from threading import Thread
try:
	import mechanize
except:
	print '''
	[!] Necessária a intalação do modulo mechanize.
	Debian:sudo apt-get install python-mechanize
	Arch:sudo pacman -S python2-mechanize
	Maiores informações no arquivo README.md
'''
	sys.exit()
from bs4 import BeautifulSoup
import datetime
import argparse
import threading
import urllib as u
import os

'''==============================================================================='''
def limpar():						# Limpar Tela
	if sys.platform == 'win32':		#Se plataforma Windows
		os.system('cls')			#Execute o comando "cls"
	else:							#Outras plataformas
		os.system('clear')			#Execute o comando "clear"

'''==============================================================================='''
def ajuda():
	limpar()
	print '''   ____                  _ _          _             
  / ___|__ _ _ __   __ _(_) |__  _ __(_)_ __   __ _ 
 | |   / _` | '_ \ / _` | | '_ \| '__| | '_ \ / _` |
 | |__| (_| | | | | (_| | | |_) | |  | | | | | (_| |
  \____\__,_|_| |_|\__, |_|_.__/|_|  |_|_| |_|\__,_|
                   |___/                Beta - v1.7
  Dashboard Finder

  Cangibrina 1.7 | coded by Fnkoc

uso: cangibrina-1.7.py -a -u[url] -w[wordlist] -t[threads] -g -d[DORK] -s[SAIDA] -v

Comandos:

  -h\t--help\t\tExibe esta ajuda e sai
  -u\t--url\t\tDefine site alvo
  -w\t--wordlist\tDefine wordlist (opcional)
  -v\t--verbose\tHabilita modo verbose
  -t\t--threads\tInforma número de processos a serem executados
\t\t\t(opcional, default = 10)
  -g\t--google\tBusca Google
  -d\t--dork\t\tInforma dork de busca
  -s\t--saida\t\tInforma nome do arquivo log gerado
  -n\t--nmap\t\tUtliza o Nmap para scan de portas no servidor

===============================================================================

Exemplos de uso:

python cangibrina-1.7.py -u facebook.com -w /root/diretorios.txt -t 10 -v
\tFoi utilizada uma wordlist personalizada, 10 threads, o modo verbose e o facebook.com como alvo

python cangibrina-1.7.py -u facebook.com -v
\tFoi utilizada a wordlist e threads padrões. facebook.com como alvo

python cangibrina-1.7.py -u facebook.com -g -s face -v
\tFoi utilizada a busca do painel através de requests e do google, gerando um arquivo "face" com os resultados

python cangibrina-1.7.py -u facebook.com -g -d 'inurl:login' -s face
\tFoi utilizado o facebook.com como alvo, wordlist e threads padrões, busca no google, e dork personalizada.

python cangibrina-1.7.py -u facebook.com -v -n
\tFoi utilizado o facebook.com como alvo, wordlis e threads padrões, verbose e nmap para scan de portas.

[IMPORTANTE] DORK DEVE SER ESCRITA ENTRE ASPAS SIMPLES!
'''


'''====A.R.G.U.M.E.N.T.O.S========================================================'''

parser = argparse.ArgumentParser(description = 'Cangibrina-1.6', add_help = False)
parser.add_argument('-h', '--help', action = 'store_true',
				help = 'Mostra esta ajuda e sai')
parser.add_argument('-u', '--url',
				help = 'Informa site alvo')
parser.add_argument('-w', '--wordlist',default = 'default',
				help = 'Informa wordlist a ser usada')
parser.add_argument('-v', '--verbose',
				action = 'store_true', help = 'Habilita modo verbose')
parser.add_argument('-t', '--threads',default = 10, type = int,
				help = 'Informa número de processos a serem executados\n Default=10')
parser.add_argument('-g', '--google', 
				action = 'store_true', help = 'Busca de sites')
parser.add_argument('-d', '--dork',
				nargs = '+', help = 'Dork de Busca')
parser.add_argument('-s', '--saida',
				default = 'log_busca', help = 'Informa nome do arquivo log')
parser.add_argument('-n', '--nmap',
				action = 'store_true', help = 'nmap')

args = parser.parse_args()


'''====A.D.M.-.F.I.N.D.E.R========================================================'''

def conexao(url, wl, verbose, threads):
	try:
		if url[:11] == 'http://www.':
			url = url[11:]
		elif url[:4] == 'www.':
			url = url[4:]
		elif url[:7] == 'http://':
			url = url[7:]
		url = 'http://www.%s/' % url
		conn = u.urlopen(url).getcode()
		if conn != 200:
			print ' [!] O site não pode ser alcançado'
			sys.exit()
		else:
			print '\n [+] Site está online\n Resposta: %s \n' % conn

	except Exception, e:
		print ' [!] ' + str(e) + '\n'
		sys.exit()

	try:
		if wl == 'default':
			os.chdir('Wordlist')
			diretorios = open('default', 'r')
		else:
			diretorios = open((wl), 'r')
	except Exception, e:
		print ' [!] ' + str(e) + '\n'
		sys.exit()
	'''==========================================================================='''
	try:	# Brute force
		print '\n [+] Testando...\n'
		os.chdir('..')
		os.chdir('src')
		os.chdir('Output')
		log = open(url[11:-1]+'.txt', 'w')
		'''======================================================================='''
		def robots():				# Checando Robots.txt
			print ' [!] Checando por Robots.txt'
			robots = (url + 'robots.txt')
			r_check = u.urlopen(robots).getcode()

			if r_check == 200:
				print ' [+] Robots.txt está disponível'
				log.write(robots)
			else:
				print ' [-] Robots.txt não está disponível'
			print ' [+] Arquivo log \"%s.txt\" em \"Cangibrina/src/Output\"\n' % url[11:-1]

			diretorios.close()
			if args.google:
				google(args.dork, args.saida)
			else:
				pass
			if args.nmap:
				nmap()
			else:
				pass
			sys.exit()

		'''======================================================================='''
		def brute():
			for ways in diretorios:
				final = url + ways
				if args.verbose:
					print final
				else:
					pass
				conn = u.urlopen(final).getcode()
				if conn == 200:
					print ' [+] Encontrado: %s' % final
					log.write(final)
			sys.exit()

		if __name__ == '__main__':
			time_started = datetime.datetime.now()
			for t in range(args.threads):
				Thread(target = brute).start()
						
			while 1==1:
				if threading.active_count() == 1:
					robots()
				elif threading.active_count() > 1:
					pass

	except Exception, e:
		print '\n [!] ' + str(e) + '\n'
		sys.exit()
	except KeyboardInterrupt:
		print '\n [!] Você interrompeu o programa\n'
		sys.exit()


'''====G.O.O.G.L.E================================================================'''

def google(query, saida):
	print '\n\t[!] Pesquisando no Google...\n'
	if not args.dork:
		query = 'site:' + args.url + ' ((intitle:painel controle | administracao | admin | login | entrar) | (inurl:admin | adm | login | entrar | painel | root)) ext:(php | asp | apsx)'
	else:
		query = ''.join(query)
		query = query.strip("'")
	print '[DORK] >> ' + query
	try:
		query = query.replace(' ', '+')		#Transforma lista query em string e substitui espaços por "+"
		req = 'https://www.google.com.br/search?q=%s&num=50&start=0' % query
		br = mechanize.Browser()
		br.set_handle_robots(False)						#Nega ser um bot
		br.addheaders = [('User-agent', 'chrome')]		#Adiciona User-Agent
		html = br.open(req).read()						#Puxa código HTML da página 
		soup = BeautifulSoup(html)

		log = open(saida + '.txt', 'w')
		for results in soup.findAll(attrs={'class':'g'}):	#Abra "Inspecionar elemento" em seu navegador para compreender
			for title in results.findAll('h3', attrs={'class':'r'}):
				t = title.text
				t = t.title()
			for link in results.findAll(attrs={'class':'s'}):
				l = link.cite.text
				print t
				print l + '\n'
				log.write(str(l) + '\n')
	except e:
		print ' [!]', e
		pass

	print '\n [+] Arquivo log gerado'
	print ' [+] Arquivo com log em \"Cangibrina/src/Output\"\n'


'''====N.M.A.P===================================================================='''
def nmap():
	print '\n\t[!] Iniciando Nmap...\n'
	comando = 'sudo nmap -sS -sV www.%s' %args.url
	print '\n', comando
	os.system(comando)

'''==============================================================================='''
if len(sys.argv) == 1:
	ajuda()
elif args.help:
	ajuda()
else:
	conexao(args.url, args.wordlist, args.verbose, args.threads)
