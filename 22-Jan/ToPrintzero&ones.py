import numpy as np
a=np.zeros((2,3))
b=np.array(a,dtype="int")
print(b)

a=np.ones((2,3))
b=np.array(a,dtype="int")
print(b)

a=np.full((2,3),5)
b=np.array(a,dtype="int")
print(b)

a=np.ones((2,3))
b=np.array(a,dtype="int")
print(b)

a=np.random.random((2,3))#print 0.0 to 0.9
print(a)

a=np.random.randint(1,5,(2,3))#print 1 to 4
print(a)

a=np.arange(0,10,2)#start 0 stop 10 increment by 2
print(a)

a=np.linspace(0,10,5)#cut in 5 piece
print(a)

a=np.linspace(0,10,5,dtype="int")#cut in 5 piece store in integer
print(a)

