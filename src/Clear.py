#!/usr/bin/python

import sys
import os

if sys.platform == "win32":		#Se plataforma Windows
	os.system("cls")			#Execute o comando "cls"
else:							#Outras plataformas
	os.system("clear")			#Execute o comando "clear"
