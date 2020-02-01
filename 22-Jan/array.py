import numpy as np
list=[]
row=int(input("how many row"))
col=int(input("How many col"))
for i in range (row):
    sub=[]
    for j in range(col):
        
        ele=float(input("Enter element"))
        sub.append(ele)
    list.append(sub)
b=np.array(list)    
print("Array is.:",b)

dim=b.ndim
print("Array dimension.:",dim,"D")

sh=b.shape
print("Shape.:",sh)

s=b.size
print("Size of array[Element].:",s)

isize=b.itemsize
print("Datatype size.:",isize)

dtype=b.dtype
print("Datatype.:",dtype)

b=np.array(list,dtype="int")    
print("After converting integer.:",b)
