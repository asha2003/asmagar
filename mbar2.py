import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
explode = (0.1, 0, 0, 0, 0, 0)

plt.pie(popularity, explode=explode, colors=['red', 'black', 'green', 'blue', 'yellow', 'cyan'],autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.show()
