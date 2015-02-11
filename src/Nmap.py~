#!/usr/bin/python
#coding=utf-8

__AUTOR__	= "Fnkoc"

import os
import colors

def run(url):
	try:
		print colors.green + "\n\t[+] " + colors.default + "Starting Nmap...\n"
		comando = "sudo nmap -PN -sV -sS www.%s" % url.replace("http://", "").replace("www.", "").replace("/", "")
		print "\n", comando
		os.system(comando)
	except Exception, e:
		print colors.red + " [!] " + colors.default + str(e)
