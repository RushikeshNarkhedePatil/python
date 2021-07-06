#Enter String from user and Remove Odd Index

str=input("Enter a String :  ")
a=""
for var1 in range(len(str)):
    if((var1%2)==0):
        a=a+str[var1]
    
print("Modified String After Removing Odd Index is:\t",a)