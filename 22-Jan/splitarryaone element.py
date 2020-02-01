import numpy as np
a=np.array([[10,20,30],[70,7,40],[60,40,50]])
                #           (from row)   (from column)     
print(a[1:2:,1:2:])# array[start:stop:step,start:stop:step]
print(a[0::2,0::2])
