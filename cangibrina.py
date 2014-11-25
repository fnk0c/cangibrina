#!/usr/bin/python
#coding=utf-8

#Nesta nova versão adicionei a opção de utilizar um servidor proxy HTTP para fazer as requisições
#Testei através do Wireshark e me pareceu estar funcionando corretamente
#Num futuro tentarei utilizar protocolo SOCKS, mas por hora somente HTTP
#Mudei o número de threads a serem utilizados quando não especificado. De 10 para 7

__AUTOR__	= 'Fnkoc'
__DATA__	= '23/11/14'
__VERSAO__	= '0.8.2'

'''Agradecimento especial ao Maximoz'''

import sys
sys.path.append('src/thirdparty/beautifulsoup4-4.3.2/')		#Adiciona diretório para busca de bibliotecas/modulos
from threading import Thread
try:							#O motivo de ser necessária a instalação do mechanize é porque não consegui
	import mechanize			#utlizar a biblioteca do mesmo modo que fiz com o BeautifulSoup. Se alguem souber
except:							#o motivo, favor me avisar
	print '''					
	[!] Necessária a intalação do modulo mechanize.
	
	Debian:sudo apt-get install python-mechanize
	Arch:sudo pacman -S python2-mechanize
	Windows: Maiores informações no arquivo README.md
'''
	sys.exit()
from bs4 import BeautifulSoup
import argparse
import threading
import urllib as u
import os

'''==============================================================================='''
#Defining term colors
if sys.platform == 'win32':
	red = ''
	green = ''
	yellow = ''
	default = ''
else:
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	default = '\033[00m'

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
                   |___/              Beta - v0.8.2
  Dashboard Finder

  Cangibrina 0.8.2 | coded by Fnkoc

uso: cangibrina.py -u[url] -w[wordlist] -t[threads] -g -d[DORK] -s[SAIDA] -p[PROXY] -v -n -a

Comandos:

  -h\t--help\t\tExibe esta ajuda e sai
  -u\t--url\t\tDefine site alvo
  -w\t--wordlist\tDefine wordlist (opcional)
  -v\t--verbose\tHabilita modo verbose
  -t\t--threads\tInforma número de processos a serem executados
\t\t\t(opcional, default = 10)
  -g\t--google\tBusca através dos motores Google e DuckDuckGo
  -d\t--dork\t\tInforma dork de busca
  -s\t--saida\t\tInforma nome do arquivo log gerado
  -n\t--nmap\t\tUtliza o Nmap para scan de serviços
  -a\t--user_agent\tModifica User-Agent
  -p\t--proxy\t\tUtiliza servidor proxy

===============================================================================

Exemplos de uso:

python cangibrina.py -u facebook.com -w /root/diretorios.txt -t 10 -v
\tFoi utilizada uma wordlist personalizada, 10 threads, o modo verbose e o facebook.com como alvo

python cangibrina.py -u facebook.com -v -s face_brute
\tFoi utilizada a wordlist e threads padrões. facebook.com como alvo, modo verbose e arquivo log gerado receberá o nome face_brute

python cangibrina.py -u facebook.com -g -s face -v
\tFoi utilizada a busca do painel através de requests e dos motores de busca, gerando um arquivo "face" com os resultados

python cangibrina.py -u facebook.com -g -d 'inurl:login' -s face
\tFoi utilizado o facebook.com como alvo, wordlist e threads padrões, motores de busca, e dork personalizada.

python cangibrina.py -u facebook.com -v -n
\tFoi utilizado o facebook.com como alvo, wordlist e threads padrões, verbose e nmap para scan de portas.

python cangibrina.py -u facebook.com -a
\tFoi utilizado o facebook.com como alvo, wordlist e threads padrões, e o argumento \"-a\" para modificar o user-agent

python cangibrina.py -u facebook.com -p 187.25.2.485:8080
\tFoi utilizado o facebook.com como alvo e um servidor proxy
'''
	print red + '[IMPORTANTE] DORK DEVE SER ESCRITA ENTRE ASPAS SIMPLES!\n\n' + default



'''====A.R.G.U.M.E.N.T.O.S========================================================'''

parser = argparse.ArgumentParser(description = 'Cangibrina', add_help = False)
parser.add_argument('-h', '--help', action = 'store_true',
				help = 'Mostra esta ajuda e sai')
parser.add_argument('-u', '--url',
				help = 'Informa site alvo')
parser.add_argument('-w', '--wordlist',
				help = 'Informa wordlist a ser usada')
parser.add_argument('-v', '--verbose',
				action = 'store_true', help = 'Habilita modo verbose')
parser.add_argument('-t', '--threads',default = 7, type = int,
				help = 'Informa número de processos a serem executados\n Default=10')
parser.add_argument('-g', '--google', 
				action = 'store_true', help = 'Busca de sites')
parser.add_argument('-d', '--dork',
				nargs = '+', help = 'Dork de Busca')
parser.add_argument('-s', '--saida',
				default = 'log_busca', help = 'Informa nome do arquivo log')
parser.add_argument('-n', '--nmap',
				action = 'store_true', help = 'nmap')
parser.add_argument('-a', '--user_agent',
				action = 'store_true', help = 'Habilita user agent')
parser.add_argument('-p', '--proxy',
				help = 'Utiliza servidor proxy')

args = parser.parse_args()


'''====A.D.M.-.F.I.N.D.E.R========================================================'''

def conexao(url, wl, verbose, threads, saida, user_agent):
	try:
		if url[:11] == 'http://www.':
			url = url[11:]
		elif url[:4] == 'www.':
			url = url[4:]
		elif url[:7] == 'http://':
			url = url[7:]
		url = 'http://www.%s/' % url
		
		'''====P.R.O.X.Y=========================================================='''

		if args.proxy:
			proxies = {'http': 'http://' + args.proxy}		#Define endereço servidor proxy
		else:
			proxies = {}									#Para não utilizar proxy
		
		'''====A.G.E.N.T=========================================================='''
		
		if args.user_agent:
			br = mechanize.Browser()
			
			if args.proxy:							#Se argumento proxy estiver sendo utilizado
				br.set_proxies(proxies)				#Definir proxy
			
			user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
			header = {'User-Agent' : user_agent}
			br.set_handle_robots(False)						#Nega ser um bot
			br.addheaders = [('User-agent', 'Firefox')]		#Adiciona User-Agent
			conn = br.open(url)			#Abre url
			real = conn.geturl()							#Verifica redirecionamento
			conn = conn.code								#Verifica codigo HTTP
		
		else:
			conn = u.urlopen(url, proxies=proxies).getcode()		#Verifica codigo HTTP
			real = u.urlopen(url, proxies=proxies).geturl()			#Recebe a URL verdadeira

		
		'''====S.T.A.T.U.S..&..R.E.D.I.R.E.C.T===================================='''
		
		if conn != 200:															#Verifica se o site está acessivel
			print red + ' [!] ' + default + 'O site não pode ser alcançado'
			
			if conn == 403:														#Caso de 403 ele retorna uma dica
				print red + ' [!] ' + default + 'Permissão Negada (Forbidden). Tente trocar o User-Agent ("-a")'

			print conn
			sys.exit()
			
		else:
			print green + '\n [+] ' + default + 'Site está online\n Resposta: %s \n' % conn

		if real != url:										#Verifica se a URL especificada é a mesma que a recebida
			print red + ' [!] ' + default + 'Site está nos redirecionado para: \n'
			print real
			keep = raw_input('\nDeseja deseja ser redirecionado? [Y]es [N]o [A]bort\n >> ').lower() #"lower" serve para converter a string
																						#de caps lock para caixa baixa ("A" ==> "a")
			
			if keep == 'n':
				pass
			elif keep == 'a':
				print red + ' [!] ' + default + 'Execução abortada\n'
				sys.exit()
			else:
				url = real
		else:
			pass
			
	except Exception, e:					#Except necessário pois o mechanize não sabe lidar com codigo 404. Ou eu não sei lidar com o mechanize
		print red + ' [!] ' + default + str(e) + '\n'
		sys.exit()
		
		
	'''====W.O.R.D.L.I.S.T========================================================'''
	try:
		if args.wordlist:			#Caso seja específicada uma wordlist
			diretorios = open((wl), 'r')
	
		else:
			os.chdir('Wordlist')	#Caso NÃO sejá especificada uma wordlist será usada a padrão
			diretorios = open('default', 'r')
			os.chdir('..')
			
	except Exception, e:
		print red + ' [!] ' + default + str(e) + '\n'
		sys.exit()

	'''==========================================================================='''
	try:	# Brute force
		print green + '\n [+] ' + default + 'Testando...\n'
		os.chdir('src')
		os.chdir('Output')						#Selecionando diretório onde será criado o log
		
		if args.saida:
			log = open(args.saida + '.txt', 'w')
		else:
			log = open('brute_cpanel.txt', 'w')

		'''======================================================================='''
		def robots():							# Checando Robots.txt
			print yellow + ' [!] ' + default + 'Checando por Robots.txt'
			robots = (url + 'robots.txt')
			r_check = u.urlopen(robots, proxies=proxies).getcode()

			if r_check == 200:
				print green + ' [+] ' + default + 'Robots.txt está disponível'
				log.write(robots)
			else:
				print red + ' [-] ' + default + 'Robots.txt não está disponível'
			print green + ' [+] ' + default + 'Arquivo log \"%s.txt\" em \"Cangibrina/src/Output\"\n' % log

			diretorios.close()
			if args.google:
				DuckDuckGo(args.dork, args.saida)
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
			for ways in diretorios:				#Ssendo "ways" os diretórios contidos no txt e "diretorios" o arquivo txt
				final = url + ways
				
				if args.verbose:
					print final
				else:
					pass

				try:				#Por esta parte ser uma cópia de um trexo acima, não vejo necessidade de comentar
					if args.user_agent:
						br = mechanize.Browser()
						
						if args.proxy:
							br.set_proxies(proxies)
						
						user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
						header = {'User-Agent' : user_agent}
						br.set_handle_robots(False)						
						br.addheaders = [('User-agent', 'Firefox')]		
						conn = br.open(final).code						

					else:
						conn = u.urlopen(final, proxies=proxies).getcode()
						
					if conn == 200:
						print green + ' [+] ' + default + 'Encontrado: %s' % final
						log.write(final)
					elif conn == 301:
						print green + ' [+] ' + default + 'Redirecionado: %s' % final
					elif conn == 404:
						if args.verbose:
							print red + ' [-] ' + default + 'HTTP Error 404: Not Found'
			
				except Exception, e:
					if args.verbose:
						print red + ' [!] ' + default + str(e)
					pass
			
			sys.exit()

		if __name__ == '__main__':
			for t in range(args.threads):
				Thread(target = brute).start()
						
			while 1==1:								#Durante a execução do programa é checado o número de threads
				if threading.active_count() == 1:	#sendo executados. Quando for igual a um significa que o brute force 
					robots()						#já foi concluido, podendo assim seguir para as proximas etapas
				elif threading.active_count() > 1:
					pass

	except Exception, e:
		print red + '\n [!] ' + default + str(e) + '\n'
		sys.exit()
	except KeyboardInterrupt:
		print red + '\n [!] ' + default + 'Você interrompeu o programa\n'
		sys.exit()


'''====D.U.C.K.D.U.C.K.G.O========================================================'''

def DuckDuckGo(query, saida):
	print green + '\n\t[!] ' + default + 'Pesquisando no DuckDuckGo...\n'
	if not args.dork:
		query = 'site:' + args.url.replace('http://', '') + ' inurl:(login/|adm/|admin/|admin/account|/controlpanel|/adminLogin|admin/adminLogin|adminitem/|adminitems/|administrator/|administration/|admin_area/|manager/|letmein/|superuser/|access/|sysadm/|superman/|supervisor/|control/|member/|members/|user/|cp/|uvpanel/|manage/|management/|signin/|log-in/|log_in/|sign_in/|sign-in/|users/|accounts/)'
	else:
		query = ''.join(query)							#Transforma lista em string 
		query = query.strip("'")						#Remove aspas simples
	print yellow + '[DORK]' + default +' >> ' + query

	try:
		query = query.replace(' ', '+')					#Substitui espaços por "+"
		req = 'http://duckduckgo.com/html/?q=%s' % query
		html = u.urlopen(req).read()
		soup = BeautifulSoup(html)

		log = open(saida + '_duck.txt', 'w')			#A parte do for é basicamente analisar a estrutura do 
														#site, para assim, saber quais serão as classes que lhe interessam
		for results in soup.findAll('div', attrs={'class':'links_main links_deep'}):
			for title in results.findAll('a', attrs={'class':'large'}):
				t = title.text
				t = t.title()
			for link in results.findAll('a', attrs={'class':'large'}):
				l = link.get('href')
				print t
				print l + '\n'
				log.write(str(l) + '\n')
	except:
		pass

	print green + '\n [+] ' + default + 'Arquivo log gerado'
	print green + ' [+] ' + default + 'Arquivo com log em \"Cangibrina/src/Output\"\n'


'''====G.O.O.G.L.E================================================================'''

def google(query, saida):
	print green + '\n\t[!] ' + default + 'Pesquisando no Google...\n'
	if not args.dork:
		query = 'site:' + args.url.replace('http://', '') + ' inurl:(login/|adm/|admin/|admin/account|/controlpanel|/adminLogin|admin/adminLogin|adminitem/|adminitems/|administrator/|administration/|admin_area/|manager/|letmein/|superuser/|access/|sysadm/|superman/|supervisor/|control/|member/|members/|user/|cp/|uvpanel/|manage/|management/|signin/|log-in/|log_in/|sign_in/|sign-in/|users/|accounts/)'
	else:
		query = ''.join(query)							#Transforma lista query em string e 
		query = query.strip("'")						#Remove aspas simples
	print yellow + '[DORK]' + default +' >> ' + query

	try:
		query = query.replace(' ', '+')					#Substitui espaços por "+"
		req = 'https://www.google.com.br/search?q=%s&num=50&start=0' % query
		br = mechanize.Browser()
		br.set_handle_robots(False)						#Nega ser um bot
		br.addheaders = [('User-agent', 'chrome')]		#Adiciona User-Agent
		html = br.open(req).read()						#Puxa código HTML da página 
		soup = BeautifulSoup(html)

		log = open(saida + '_google.txt', 'w')
		for results in soup.findAll(attrs={'class':'g'}):	#Abra "Inspecionar elemento" em seu navegador para compreender
			for title in results.findAll('h3', attrs={'class':'r'}):
				t = title.text
				t = t.title()
			for link in results.findAll(attrs={'class':'s'}):
				l = link.cite.text
				print t
				print l + '\n'
				log.write(str(l) + '\n')
	except:
		pass

	print green + ' [+] ' + default + 'Arquivo log gerado'
	print green + ' [+] ' + default + 'Arquivo com log em \"Cangibrina/src/Output\"\n'


'''====N.M.A.P===================================================================='''

def nmap():		#Talvez num futuro eu permita a execução de um comando personalizado
	print green + '\n\t[+] ' + default + 'Iniciando Nmap...\n'
	comando = 'sudo nmap -PN -sV -sS www.%s' %args.url.replace('http://', '').replace('www.', '')
	print '\n', comando
	os.system(comando)

'''==============================================================================='''
if len(sys.argv) == 1:		#Caso o número de argumentos seja igual a 1, ou seja, apenas o nome do programa
	ajuda()					#a ajuda será exibida
elif args.help:
	ajuda()
else:
	conexao(args.url, args.wordlist, args.verbose, args.threads, args.saida, args.user_agent)
