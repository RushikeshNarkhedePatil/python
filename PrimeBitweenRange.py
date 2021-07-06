"""
Prime Number bitween range 
"""
start =int(input("Enter Starting Number : \n"))
end = int(input("Enter Ending Number :\n"))
print("Prime Number Bitween Range is :")
for i in range(start, end+1):
    if  i>1:
	    for j in range(2,i):
		    if(i % j==0):
			    break
	    else:
		    print(i)
