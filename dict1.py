import operator
x = {1: 2, 2: 4, 3: 3, 4: 1, 5: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
dict = {'Name': 'Zara', 'Age': 'seven', 'Class': 'First'}
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))
print(sorted_dict)