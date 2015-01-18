#!/usr/bin/python

__AUTOR__	= "Fnkoc"

import sys

if sys.platform == "win32":
	red = ""
	green = ""
	yellow = ""
	default = ""
else:
	red = "\033[31m"
	green = "\033[32m"
	yellow = "\033[33m"
	default = "\033[00m"
