"""
Enter String and Count Alphabet and Digit
"""

str=input("Enter String")
d=a=0
for var1 in str:
    if var1.isdigit():
        d=d+1
    elif var1.isalpha():
        a=a+1
    else:
        print("Special character not allowd")
print("Latter count is:",a)
print("Digit Count is:",d)
