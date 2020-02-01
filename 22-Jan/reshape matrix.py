import numpy as np
a=np.array([[2,3],[4,5],[6,7]])
print(a)

b=a.reshape((2,3))#regshape the given matrix
print(b)

b=a.reshape((6,1))
print(b)
