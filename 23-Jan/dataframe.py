import pandas as pd
dic={'a':[1,2,7,5],'b':[3,4,8,9],'c':[5,6,3,2],'d':[7,8,1,0]}
df=pd.DataFrame(dic,columns=('a','b'))
print(df)
print("Print only a column")
print(df[["a","b"]])
