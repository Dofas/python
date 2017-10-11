#! /usr/bin/env python3
s=input('zadayte r9dok ').split(' ')
b=list(s)
k=sorted(b,key=len)
u = ' '.join(k)
print(u)
