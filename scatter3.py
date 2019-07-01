import matplotlib.pyplot as plt
from pylab import randn
import random
import math
no_of_balls=25
x=randn(no_of_balls)
y=randn(no_of_balls)
colors=[random.randint(1, 4) for i in range(no_of_balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(no_of_balls)]
plt.scatter(x,y,s=areas,c=colors )
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
