#!/usr/bin/python

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


from mechanize import Browser
try:
	import urllib2 as u
except:
	import urllib.request as u

class tor(object):
	def __init__(self):
		pass

	def connect(self):
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
			print(" [-] " + str(e))
			print(" [!] " + "Check if TOR is running on 127.0.0.1:9050")
			exit()

class conn(object):
	def __init__(self, target, agent):
		self.target = target
		self.agent = agent

	def HTTPcode(self):
		try:
			if self.agent == True:
				br = Browser()

				UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
				header = {"User-Agent" : UserAgent}
				br.set_handle_robots(False)
				br.addheaders = [("User-agent", "Fifefox")]
				
				resp = br.open(self.target).code

			else:
				resp = u.urlopen(self.target).getcode()
	
			return(resp)
		except u.HTTPError:
			return(404)
	
	def redirect(self):
		try:
			if self.agent == True:
				br = Browser()

				UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
				header = {"User-Agent" : UserAgent}
				br.set_handle_robots(False)
				br.addheaders = [("User-agent", "Fifefox")]
				
				remote_url = br.open(self.target).geturl()

			else:
				remote_url = u.urlopen(self.target).geturl()

			return(remote_url)
		except Exception as e:
			print(e)
