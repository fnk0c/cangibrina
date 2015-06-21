#!/usr/bin/python

__AUTOR__	= "Fnkoc"

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

import sys
import os

if sys.platform == "win32":		#Se plataforma Windows
	os.system("cls")			#Execute o comando "cls"
else:							#Outras plataformas
	os.system("clear")			#Execute o comando "clear"
