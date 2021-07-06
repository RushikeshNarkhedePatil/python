"""
Number Convert Decimal to binary hexadecimal and Octal

"""
print("Enter your Choice :- \n")
print("Do you Want to Conver Decimal To: \nBinary Then Press : 1\nOctal Then Press:  2\nHexadecimal Then Press:  3\n")
a=int(input())

if(a==1):
    b=int(input("Enter Number :\n"))
    c=bin(b)
    print("Decimal To binary is: ",c)
elif(a==2):
     b=int(input("Enter Number :\n"))
     c=oct(b)
     print("Decimal To Octal is: ",c)
elif(a==3):
     b=int(input("Enter Number :\n"))
     c=hex(b)
     print("Decimal To HexaDecimal  is: ",c)
else:
    print("Enter Valid Choice :- 1 To  3")
