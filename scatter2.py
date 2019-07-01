import matplotlib.pyplot as plt
from pylab import randn
x=randn(200)
y=randn(200)
plt.scatter(x,y,s=70, facecolors='none', edgecolors='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()