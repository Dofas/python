#! /usr/bin/env python3

a = list(input("Введіть речення : "))

i = 0 
while i < len(a):
	if a[i] == " " and a[i + 1] == " ":
		while a[i+1]==" ":
			a.pop(i+1)
	i = i + 1
k = ''.join(a)
print(k)
