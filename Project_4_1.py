#! /usr/bin/env python3

import math

a1 = input("Задайте змінну а : ")
b1 = input("Задайте змінну b : ")
a=float(a1)
b=float(b1)
if b == 0:
	while b == 0:
		b = int(input("Введіть змінну b, b ≠ 0 : "))
		if b == 0:
			continue
		else:
		    print("Вихідні дані: ", (math.sqrt(a*b))/(math.exp(a)*b)+(a*math.exp(((2*a)/b))))
else:
    print("Вихідні дані : ", (math.sqrt(a*b))/(math.exp(a)*b)+(a*math.exp(((2*a)/b))))

