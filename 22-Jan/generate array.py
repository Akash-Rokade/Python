import numpy as np
l=[]
row=int(input("How many row "))
col=int(input("How many col "))

num=row*col

for i in range (num):
    ele=int(input("Enter Element "))
    l.append(ele)
a=np.array(l)
b=a.reshape(row,col)
print(b)
