#!/usr/bin/python
#coding=utf-8

__AUTOR__	= "Fnkoc"

import sys

try:
	from bs4 import BeautifulSoup

except:
	print("""
 [!] Please install BeautifulSoup!

 Debian: sudo apt-get install python-beautifulsoup       
 Arch: sudo pacman -S python2-beautifulsoup4  
 Windows => see READEME.md""")

import mechanize
import colors
import urllib as u
import os

'''====D.U.C.K.D.U.C.K.G.O========================================================'''

def DuckDuckGo(query, saida, url):
	print (colors.green + "\n\t[!] " + colors.default + "Searching on DuckDuckGo...\n")
	if query == None:
		query = "site:" + url.replace("http://", "") + " inurl:(login/|adm/|admin/|admin/account|/controlpanel|/adminLogin|admin/adminLogin|adminitem/|adminitems/|administrator/|administration/|admin_area/|manager/|letmein/|superuser/|access/|sysadm/|superman/|supervisor/|control/|member/|members/|user/|cp/|uvpanel/|manage/|management/|signin/|log-in/|log_in/|sign_in/|sign-in/|users/|accounts/)"

	else:
		query = "".join(query)							#Transforma lista em string 
		query = query.strip("'")						#Remove aspas simples
	print (colors.yellow + "[DORK]" + colors.default +" >> " + query)

	try:
		query = query.replace(" ", "+")					#Substitui espaços por "+"
		req = "http://duckduckgo.com/html/?q=%s" % query
		html = u.urlopen(req).read()
		soup = BeautifulSoup(html)

		log = open(saida + "_duck.txt", "w")			#A parte do for é basicamente analisar a estrutura do 
														#site, para assim, saber quais serão as classes que lhe interessam
		for results in soup.findAll("div", attrs={"class":"links_main links_deep"}):
			for title in results.findAll("a", attrs={"class":"large"}):
				t = title.text
				t = t.title()
			for link in results.findAll("a", attrs={"class":"large"}):
				l = link.get("href")
				print (t)
				print (l + "\n")
				log.write(str(l) + "\n")
	except:
		pass

	log.close()
	print (colors.green + "\n [+] " + colors.default + "Log file has been generated")
	print (colors.green + " [+] " + colors.default + "Log file at \"Cangibrina/output\"\n")


'''====G.O.O.G.L.E================================================================'''

def google(query, saida, url):
	print (colors.green + "\n\t[!] " + colors.default + "Searching on Google...\n")

	if query == None:
		query = "site:" + url.replace("http://", "") + " inurl:(login/|adm/|admin/|admin/account|/controlpanel|/adminLogin|admin/adminLogin|adminitem/|adminitems/|administrator/|administration/|admin_area/|manager/|letmein/|superuser/|access/|sysadm/|superman/|supervisor/|control/|member/|members/|user/|cp/|uvpanel/|manage/|management/|signin/|log-in/|log_in/|sign_in/|sign-in/|users/|accounts/)"
	else:
		query = "".join(query)							#Transforma lista query em string e 
		query = query.strip("'")						#Remove aspas simples

	print (colors.yellow + "[DORK]" + colors.default +" >> " + query)

	try:
		query = query.replace(" ", "+")					#Substitui espaços por "+"
		req = "https://www.google.com.br/search?q=%s&num=50&start=0" % query
		br = mechanize.Browser()
		br.set_handle_robots(False)						#Nega ser um bot
		br.addheaders = [("User-agent", "chrome")]		#Adiciona User-Agent
		html = br.open(req).read()						#Puxa código HTML da página 
		soup = BeautifulSoup(html)

		log = open(saida + "_google.txt", "w")
		for results in soup.findAll(attrs={"class":"g"}):	#Abra "Inspecionar elemento" em seu navegador para compreender
			for title in results.findAll("h3", attrs={"class":"r"}):
				t = title.text
				t = t.title()
			for link in results.findAll(attrs={"class":"s"}):
				l = link.cite.text
				print (t)
				print (l + '\n')
				log.write(str(l) + '\n')
	except:
		pass

	log.close()
	print (colors.green + " [+] " + colors.default + "Log file has been generated")
	print (colors.green + ' [+] ' + colors.default + 'Log file at \"Cangibrina/output\"\n')
