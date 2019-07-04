import matplotlib.pyplot as plt
with open("test1.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
print(x)
l1=[]
for i in x:
    l1.append(int(i))
l2=[]
for i in y:
    l2.append(int(i))
print(y)
plt.plot(l1, l2)

plt.xlabel('x - axis')

plt.ylabel('y - axis')
plt.title('Sample graph!')

plt.show()
