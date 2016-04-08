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

from sys import path
import argparse
path.append("src")
import connection
import scans
from time import sleep
from threading import Thread, active_count

parser = argparse.ArgumentParser(description = "Fast and powerful admin finder")

parser.add_argument("-u", help = "target site", type = str, required = True)

parser.add_argument("-w", help = "set wordlist (default: wl_medium)", \
					default = "./wordlists/wl_medium")

parser.add_argument("-t", help = "set threads number (default: 5)", default = 5\
					, type = int)

parser.add_argument("-v", help = "enable verbose", \
					default = False, required = False, action = "store_true")

parser.add_argument("--ext", help = "filter path by target extension",\
					default = False)

parser.add_argument("--user-agent", help = "modify user-agent", default = False,\
					action = "store_true", dest = "UserAgent")

parser.add_argument("--tor", help = "set TOR proxy", default = False, action = \
					"store_true")

parser.add_argument("--search", help = "use google and duckduckgo to search", \
					action = "store_true")

parser.add_argument("--dork", help = "set custom dork", default = None)

parser.add_argument("--nmap", help = "use nmap to scan ports and services", \
					nargs = "?", default = False)
args = parser.parse_args()

def check_target(target, UserAgent, tor):
	if tor != False:
		connection.tor().connect()
	else:
		pass

	conn = connection.conn(target, UserAgent)
	HTTPcode = conn.HTTPcode()
	if HTTPcode == 200:
		print("Server status: Online (%s)" % HTTPcode)
	else:
		print("Server status: Offline (%s)" % HTTPcode)

	redirect = conn.redirect()

	if target != redirect:
		print("Redirected: %s" % redirect)
		answer = raw_input("Follow redirection? [y/N] ").lower()
		
		if answer == "n" or answer == "":
			return(target)

		elif answer != "" or answer != "n":
			print("\nNew target: %s" % redirect)
			return(redirect)

def brute(target, paths, ext, UserAgent, tor, found):
	def ItsTime():
		url_target = "%s/%s" % (target, path)
		paths.remove(path)

		conn = connection.conn(url_target, UserAgent)
		HTTPcode = conn.HTTPcode()

		if HTTPcode == 200:
			print("Found: %s >> (%s)" % (url_target, HTTPcode))
			found.append(url_target)
			
		if HTTPcode == 301:
			print("Redirected %s >> (%a)" % (url_target, HTTPcode))
		
		if HTTPcode == 404:
			if args.v != False:
				print(url_target + " >> " + str(HTTPcode))
			else:
				pass

	for path in paths:
		if ext != False:
			if "." in path:
				if ext in path:
					ItsTime()
				else:
					pass						
			else:
				ItsTime()
		else:
			ItsTime()

if __name__ == "__main__":
	import banner
	
	print("\n")
	print("*" * 80)
	
	if args.u[:7] != "http://":
		target = "http://%s" % args.u
	elif args.u[:7] == "http://":
		target = args.u

	target_result = check_target(target, args.UserAgent, args.tor)

	paths = []
	with open(args.w, "r") as wordlist:
		paths = wordlist.readlines()

	found = []
	
	print(" [+] Testing...")
	for j in range(args.t):
		Thread(target = (brute), args = (target_result, paths, args.ext,\
		args.UserAgent, args.tor, found)).start()
		sleep(1.2)

	loop = True

	while loop == True:
		if active_count() == 1:
			loop = False
			if args.search != False:
				s = scans.passive(target_result, args.dork)
				s.google()
				s.DuckDuckGo()

			if args.nmap != False:
				if args.nmap == None:
					n = scans.active(target_result.replace("http://", "")\
					.replace("https://", ""))
					n.nmap("sudo nmap -v -sS -sC")

				elif args.nmap != None:
					n = scans.active(None)
					n.nmap(args.nmap)

			robots = target_result + "/robots.txt"
			rob_code = connection.conn(robots, args.UserAgent).HTTPcode()
			if rob_code == 200:
				print("Found: %s >> (%s)" % (robots, rob_code))
				found.append(robots)
			else:
				if args.v != False:
					print(robots + " >> " + str(rob_code))
				else:
					pass
			print("*" * 80)
			print("\t[RESULTS]")
			for k in found:
				print(k)

		elif active_count() > 1:
			loop = True
