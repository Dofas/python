#! /usr/bin/env python3

def per (a1,a2,obs):
	i1=0
	i2=0
	s=0
	while i1<int(len(a1)):
		while i2<int(len(a2)):
			if a2[i2]==a1[i1]:
				s=s+1
				print(s)
			i2=i2+1
		i1=i1+1
	if (s==int(len(a2))) and (obs==1):
		print('Z perwogo r9dka mozna ytworutu drygui')
	elif (s==int(len(a2))) and (obs==2):
		print('Z drygogo r9dka mozna ytworutu perwui')
	else:
		print('Ytworenn9 nemozluve')
	print(s)
s1=input('Zadayte perwui r9dok ')
s2=input('Zadayte drygui r9dok ')
obs=1
if len(s1)>len(s2):
	per(s1,s2,obs)
elif len(s2)>len(s1):
	obs=obs+1
	per(s2,s1,obs)
else:
	per(s1,s2,obs)
