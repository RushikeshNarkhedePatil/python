#  Remove Duplicate Element
List1=[22,23,22,34,23,4,33,55,77,23,22]
final_list = []
for num in List1:
     if num not in final_list:
        final_list.append(num)
print("Input List",List1)
print("Final List after Removing Duplicate Element : ",final_list)