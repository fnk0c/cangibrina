#!/usr/bin/python
#coding=utf-8

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

###########[PERIGO]#############
#Gambiarra fudida neste arquivo#
################################
#A gambiarra em questão é o fato de eu ter dado ctrl + c ctrl + v
#do código inteiro por causa de duas linhas.
#linha  47 e 52, linhas responsáveis por identificar o redirecionamento
#Caso haja redirecionamento vá para a linha 67

__AUTOR__	= "Fnkoc"

import sys

try:
	import mechanize
except:
	print("""
 [!] Please install Mechanize!

 Debian/Ubuntu => apt-get install python-mechanize
 Arch/Manjaro => pacman -S python2-mechanize
 Windows => see README.md""")

import urllib as u
import colors

global log
py_log = []

def redirect_tester(url, proxy, user_agent, verbose):
	'''====P.R.O.X.Y=========================================================='''

	if proxy:
		proxies = {"http": "http://" + proxy}		#Define endereço servidor proxy
	else:
		proxies = {}								#Para não utilizar proxy
		
	'''====A.G.E.N.T=========================================================='''

	try:
		if user_agent:
			br = mechanize.Browser()
			
			if proxy:									#Se argumento proxy estiver sendo utilizado
				br.set_proxies(proxies)					#Definir proxy
			
			UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
			header = {"User-Agent" : UserAgent}
			br.set_handle_robots(False)					#Nega ser um bot
			br.addheaders = [("User-agent", "Firefox")]	#Adiciona User-Agent
			conn = br.open(url)							#Abre url

			real = conn.geturl()						#Verifica redirecionamento
			conn = conn.code							#Verifica codigo HTTP			

		else:
			conn = u.urlopen(url, proxies=proxies).getcode()
			real = u.urlopen(url, proxies=proxies).geturl()	#Recebe a URL verdadeira

		if conn == 200:
			print(colors.green + " [+] " + colors.default + "Site is up\n code: %s\n") % (conn)

		elif conn == 403:
			print(colors.red + " [!] " + colors.default + "Forbidden: %s | %s |") % (url, conn)
			print(" Try to change your User-Agent (\"-a\")")
			sys.exit()

		elif conn == 404:
			if verbose:
				print(colors.red + " [-] " + colors.default + "HTTP Error 404: Not Found")

		else:
			print("Response Code: %s") % conn
	
		if real != url:										#Verifica se a URL especificada é a mesma que a recebida
			print(colors.red + " [!] " + colors.default + "Site is redirecting us to: \n")
			print(real)
			keep = raw_input("\nWould you like to follow the redirection?? [Y]es [N]o [A]bort\n >> ").lower()   #"lower" serve para converter a string
																												#de caps lock para caixa baixa ("A" ==> "a")
			if keep == "n":
				pass
			elif keep == "a":
				print(colors.red + " [!] " + colors.default + "Aborted\n")
				sys.exit()
			else:
				url = real
		else:
			pass

	except Exception as e:
		if verbose:
			print(colors.red + " [!] " + colors.default + str(e))
		sys.exit()


def tester(url, proxy, user_agent, verbose, saida):
	'''====P.R.O.X.Y=========================================================='''

	if proxy:
		proxies = {"http": "http://" + proxy}		#Define endereço servidor proxy
	else:
		proxies = {}								#Para não utilizar proxy
		
	'''====A.G.E.N.T=========================================================='''

	try:				
		if user_agent:
			br = mechanize.Browser()

			if proxy:									#Se argumento proxy estiver sendo utilizado
				br.set_proxies(proxies)					#Definir proxy
			
			UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
			header = {"User-Agent" : UserAgent}
			br.set_handle_robots(False)					#Nega ser um bot
			br.addheaders = [("User-agent", "Firefox")]	#Adiciona User-Agent

			
			conn = br.open(url)							#Abre url
			conn = conn.code							#Verifica codigo HTTP			

		else:
			conn = u.urlopen(url, proxies=proxies).getcode()

		if conn == 200:
			print(colors.green + " [+] " + colors.default + "Found: %s | %s |") % (url, conn)
			py_log.append(url)
			py_log.append(conn)

		elif conn == 301:
			print(colors.green + " [+] " + colors.default + "Redirecting: %s | %s |") % (url, conn)
			py_log.append(url)
			py_log.append(conn)
		
		elif conn == 403:
			print(colors.red + " [!] " + colors.default + "Forbidden: %s | %s |") % (url, conn)
			print(" Try to change your User-Agent (\"-a\")")
			log.append(url)
			log.append(conn)

		elif conn == 404:
			if verbose:
				print(colors.red + " [-] " + colors.default + "HTTP Error 404: Not Found")

		else:
			print(colors.red + " [!] " + colors.default + str(url))
			print("Response Code: %s") % conn

	except Exception as e:
		if verbose:
			print(colors.red + " [!] " + colors.default + str(e))
		pass

def result(log):
	for l in py_log:
		print (colors.green + " [+] " + colors.default + str(l))

	if log:
		with open("log.txt", "w") as txt_log:
			txt_log.write(str(py_log))
