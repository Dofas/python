#! /usr/bin/env python3

k = input("Zadayte r9dok : ").split()
i = 0 
mas = []
while i < len(k):
	mas.append(len(k[i]))
	i = i + 1
print(min(mas))
