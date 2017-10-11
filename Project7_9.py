#! /usr/bin/env python3
a=input('Zadayte nomer kvutka ')
k=len(a)
def par(a):
	j=a[::-1]
	i=0
	s1=0
	s2=0
	u=int(len(a)/2)
	while i<u:
		s1=s1+int(a[i])
		s2=s2+int(j[i])
		i=i+1
	if (s1==s2):
		print('Omg u are so lucky')
	else:
		print('ahahahah u are lox')
def nepar(r1,r2):
	i=0
	s1=0
	s2=0
	while i<int(len(r1)):
		s1=s1+int(r1[i])
		s2=s2+int(r2[i])
		i=i+1
	if (s1==s2):
		print('Omg u are so lucky')
	else:
		print('ahahah u are lox')
if k//2==0:
	par(a)
else:
	y=int(len(a)//2)
	r1=a[0:y]
	r2=a[y+1:k]
	nepar(r1,r2)
	
