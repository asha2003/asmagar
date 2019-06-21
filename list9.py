def onecommon(list1,list2):
    result = False

    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result

    return result

a=[]
b=[]
print("Enter 1st Array Elements")
for i in range(4):
    a.append(input())
print("Enter 2nd Array Elements")
for i in range(4):
    b.append(input())

print(onecommon(a,b))
