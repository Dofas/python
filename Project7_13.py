#! /usr/bin/env python3
s1=input('Zadayte perwui r9dok ')
s2=input('Zadayte drygui r9dok ')
s=0
if len(s1)>len(s2):
	i1=0
	i2=0
	while i1<len(s1):
		if i2<len(s2):
			while i2<len(s2):
				print(s1[i1],' ce z 1 ',s2[i2],' ce z 2')
		i2=i2+1
		i1=i1+1
