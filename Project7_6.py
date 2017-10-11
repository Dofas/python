#! /usr/bin/env python3
def zvezda(a): 
	i = 0
	star = ""
	while i < len(a) + 2:
		star = star + "*"
		i = i + 1 
	print(star + "\n*" + a + "*\n" + star)

a = input("Введіть строку : ")

zvezda(a)
