from array import *
newarray = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(newarray))
print("enter element")
search_ele=int(input())
print("Number of occurrences of the number  in the said array: "+str(newarray.count(search_ele)))