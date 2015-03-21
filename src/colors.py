#!/usr/bin/python

__AUTOR__	= "Fnkoc"

import sys

if sys.platform == "win32":
	red = ""
	white = ""
	green = ""
	yellow = ""
	default = ""
else:
	red = "\033[31m"
	white = "\033[1;37m"
	green = "\033[32m"
	yellow = "\033[33m"
	default = "\033[00m"
