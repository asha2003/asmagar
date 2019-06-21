strlist = ['asha', 'a', 'aba']
count = 0
for i in strlist:
    length = len(i)
    if len(i) >= 2 and i[0]==i[length-1]:
        count = count+1

print(count)

