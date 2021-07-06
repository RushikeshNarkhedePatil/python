"""
calculate a students’s result based on two examinations
"""
var1=int(input("Enter Marks of Sport event: "))
var2=int(input("Enter Marks of Activity: "))
marks = (var1+var2)*100/100
print("Your Marks in Percentage is ",marks)
if marks>=50:
 print("You are Passed!")
else:
 print("You are failed")