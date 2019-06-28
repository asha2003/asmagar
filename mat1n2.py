import matplotlib.pyplot as plt
import matplotlib
matplotlib.get_backend()
X = [1,2,3,4,5]
Y = [10,20,30,40,50]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()