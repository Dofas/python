#! /usr/bin/env python3

def sor(a):
	s = []
	i = 0
	l = len(a)
	while i < l:
		m = min(a)
		a.remove(m)
		s.append(m)
		print(s)
		i = i + 1

a = list(input('Zadayte spusok dl9 sortyvann9 (zna4enn9 zadavatu bez probeliv) : '))

sor(a)

