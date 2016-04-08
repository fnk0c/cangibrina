#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__DATE__	= "08/04/16"
__VERSION__	= "0.8.6"
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


from bs4 import BeautifulSoup
from mechanize import Browser
from subprocess import check_call

class passive(object):
	def __init__(self, target, dork):
		self.target = target
		self.dork = dork

	def google(self):
		print("\n\t[!] Searching on Google...\n")

		if self.dork == None:
			query = "site:" + self.target.replace("http://", "").replace("https://", "") + " inurl:(login||adm||admin||admin/account||controlpanel||adminitem||adminitems||administrator||administration||admin_area||manager||letmein||superuser||access||sysadm||superman||supervisor||control||member||members||user||cp||uvpanel||manage||management||signin||log-in||log_in||sign_in||sign-in||users||account)"
		else:
			query = "".join(self.dork)
			query = query.strip("'")

		print("[DORK] >> " + query)

		try:
			query = query.replace(" ", "+")
			req = "https://www.google.com.br/search?q=%s&num=50&start=0" % query
			br = Browser()
			br.set_handle_robots(False)
			br.addheaders = [("User-agent", "chrome")]
			html = br.open(req).read() 
			soup = BeautifulSoup(html, "html5lib")

			with open("./output/google-%s.txt" % self.target[8:], "w") as log:
				for results in soup.findAll(attrs={"class":"g"}):
					for title in results.findAll("h3", attrs={"class":"r"}):
						t = title.text
						t = t.title()
					for link in results.findAll(attrs={"class":"s"}):
						l = link.cite.text
						print (t)
						print (l + '\n')
						log.write(str(l) + '\n')
		
		except Exception as e:
			print(e)

	def DuckDuckGo(self):
		"""DuckDuckGo search"""
		print ("\n\t[!] Searching on DuckDuckGo...\n")
		if self.dork == None:
			query = "site:" + self.target.replace("http://", "").replace("https://", "") + " inurl:(login||adm||admin||admin/account||controlpanel||adminitem||adminitems||administrator||administration||admin_area||manager||letmein||superuser||access||sysadm||superman||supervisor||control||member||members||user||cp||uvpanel||manage||management||signin||log-in||log_in||sign_in||sign-in||users||accounts)"

		else:
			query = "".join(self.dork)
			query = query.strip("'")
		print("[DORK] >> " + query)

		try:
			query = query.replace(" ", "+")
			req = "http://duckduckgo.com/html/?q=%s" % query
			html = u.urlopen(req).read()
			soup = BeautifulSoup(html, "html5lib")

			with open("./output/duck-%s.txt" % self.target[8:], "w") as log:
				for results in soup.findAll("div", attrs={"class":"results"}):
					for title in results.findAll("a", attrs={"class":"result__a"}):
						t = title.text
						t = t.title()
					for link in results.findAll("a", attrs={"class":"result__url"}):
						l = link.get("href")
						print (t)
						print (l + "\n")
						log.write(str(l) + "\n")
		except:
			pass

class active(object):
	def __init__(self, target):
		self.target = target
	def nmap(self, command):
		if self.target != None:
			check_call("%s %s" % (command, self.target), shell = True)
		else:
			check_call(command, shell = True)
