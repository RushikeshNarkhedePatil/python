"""
Sum of natural number
"""
num =int(input("Enter Number  :"))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
  
   while(num > 0):
       sum = sum + num
       num = num - 1
   print("The sum is", sum)