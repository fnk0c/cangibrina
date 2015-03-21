#!/usr/bin/python

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
