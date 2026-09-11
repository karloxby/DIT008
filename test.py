'''
import random

a = random.random()
b = random.random()

while a >= b:
    a = random.random()
    b = random.random()

c = random.random()
d = random.random()

while c >= d:
    c = random.random()
    d = random.random()
'''

a = -0.10
b = 0.11
c = -10.1
d = 1.11

ac = a * c
bd = b * d

if ac < bd:
    print(f"ac = {ac:.2f} < bd = {bd:.2f}")
else:
    print(a, b, c, d, ac, bd)
