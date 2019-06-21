tup=(1,2,3,4,5,1,2,3)
set1=set()
for i in tup:
    if tup.count(i)==2:
        set1.add(i)

print(set1)
