"""
Generate 10 Integer Random Number and print Even and odd Number Seprated.
"""
import random
even=[]
odd=[]
for i in range(1,11):
 n=random.randint(1,100)
 if n%2==0:
    even.append(n)
 else:
    odd.append(n)
print(even)
print(odd)