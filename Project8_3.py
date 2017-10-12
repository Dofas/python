#! /usr/bin/env python3
def ser(a):
	i=0
	s=0
	while i<len(a):
		s=s+int(a[i])
		i=i+1
	s=s/len(a)
	return(s)
def med(e):
	k=len(e)
	if k%2==0:
		t=int(e[k//2])+int(e[k//2-1])
		return(t)
	if k//2!=0:
		return(int(e[int(k//2)]))
t=list(input('Zadayte spusok z 4uslamu (zna4enn9 zadavatu bez probeliv) : '))
print('Seredne zna4enn9 : ',ser(t),'Mediana : ',med(t))
