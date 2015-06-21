#!/usr/bin/python

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

dirs = []
pages = []
exts = []
final = []

di = open("diretorios", "r").readlines()
for d in di:
	d = d.replace("\n", "")
	dirs.append(d)

pa = open("paginas", "r").readlines()
for p in pa:
	p = p.replace("\n", "")
	pages.append(p)

ex = open("extensoes", "r").readlines()
for e in ex:
	e = e.replace("\n", "")
	exts.append(e)


for p in pages:
	for d in dirs:
		for e in exts:
			final.append(d + p + e)

with open("custom", "w") as wl:
	for p in pages:
		for e in exts:
			wl.write(p + e + "\n")
	for d in dirs:
		wl.write(d + "\n")
	for i in final:
		wl.write(str(i) + "\n")
