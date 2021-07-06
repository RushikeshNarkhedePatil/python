"""
Calculate number of  character and Digit in String
"""

str1=input("Enter a String")
d=c=count=0
for var1 in str1:
    if(var1.isdigit):
        d=d+1
    elif(var1.isalpha):
        c=c+1
    else:
        print("Special Character not allowd")
    
count=d+c
print("No digit and alphabet count is",count)