#! /usr/bin/env python3
import string
import random
a=list('~!@#$%^&*_')
b=list('0123456789')
def randompassword():
  i=random.randint(0,9)
  j=random.randint(0,9)
  chars = a[i] + string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 20)
  return ''.join(random.choice(chars) for x in range(size)) + a[i] + b[j]
print(randompassword())
