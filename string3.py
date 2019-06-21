var2 = "Python Programming"
dict={}
for i in var2:
    c=var2.count(i)
    dict2 = {i:c}
    dict.update(dict2)

print(dict)