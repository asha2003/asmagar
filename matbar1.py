import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
explode = (0.1, 0, 0, 0, 0, 0)
#plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')
plt.barh(x_pos, popularity, color='green')
plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

plt.show()