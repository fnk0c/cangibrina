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

if sys.platform == "linux2":
	red = "\033[31m"
	white = "\033[1;37m"
	green = "\033[32m"
	yellow = "\033[33m"
	default = "\033[00m"

else:
	red = ""
	white = ""
	green = ""
	yellow = ""
	default = ""
