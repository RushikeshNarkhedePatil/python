"""
Factorial number
input  : 4
output : 4*3*2*1
"""

n=int(input("Enter a Number : "))
if n < 0:
    print("")
elif n == 0 or n == 1:
     n=1
     print("Factorial no is: ",n)
else:
    fact = 1
    while(n > 1):
        fact =fact*n
        n =n-1
    print("Factorial of given no is: ",fact)