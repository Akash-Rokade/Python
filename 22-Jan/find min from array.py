import numpy as np
a=np.array([[1,2],[3,4],[4,225]])

b=a.min()
print("MINIMUM NUMBER FROM ARRAY",b)

b=a.max()
print("MAXIMUN NUMBER FROM ARRAY",b)


b=a.min(axis=0)
print("MINIMUM NUMBER from Column",b)
b=a.max(axis=0)
print("MIXIMUM NUMBER from Column",b)

b=a.min(axis=1)
print("MANIMUN NUMBER from row",b)
b=a.max(axis=1)
print("MAXIMUN NUMBER from row",b)

