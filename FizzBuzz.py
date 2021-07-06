"""
fizzBuzz Game
"""
print("****************Welcome To FizzBuzz Game*********************")
var1=int(input("Enter Starting Point : "))
var2=int(input("Enter Ending Point : "))
for i in range(var1,var2):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
        continue
    elif i%3==0:
        print ("fizz")
        continue
    elif i%5==0:
        print ("buzz")
        continue
    else:
        print(i)