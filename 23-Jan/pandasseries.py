import pandas as pd
l=[1,2,3,4,5]
indx=['a','b','c','d','e']
a=pd.Series(l,index=indx)
print(a['c'])
