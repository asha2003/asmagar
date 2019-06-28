import numpy as np
a=np.ones((3,3))
a=np.pad(a,pad_width=1,mode='constant',constant_values=0)
print(a)