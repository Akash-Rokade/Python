import numpy as np
a=np.array([[10,20],[30,40],[40,50]])
b=np.array([[1,2],[3,4],[4,5]])

c=np.add(a,b)
print("Addition ",c)

c=np.subtract(a,b)
print("Subtract",c)

c=np.multiply(a,b)
print("Multiplication ",c)

c=np.divide(a,b)
print("Divide ",c)

i=b.reshape(2,3)
c=np.matmul(a,i)
print("matMUl.:",c)




