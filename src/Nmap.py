#!/usr/bin/python
#coding=utf-8

__AUTOR__	= "Fnkoc"

import os
import colors

def run(url):
	try:
		print (colors.green + "\n[+] " + colors.default + "Starting Nmap...\n")
		comando = "sudo nmap -Pn -sC -sS -g 53 -D \'127.0.0.1\' www.%s" % url.replace("http://", "").replace("www.", "").replace("/", "")
		print ("\n%s" % comando)
		os.system(comando)
	except Exception as e:
		print (colors.red + " [!] " + colors.default + str(e))
