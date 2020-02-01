import pandas as pd
d={}
d["roll"]=[1,2,3]
d["name"]=["abc","def","xyz"]
d["marks"]=[15,25,35]

pd.DataFrame(d).to_csv("ThisisCSVfile.csv",index=False)#it doesnt store the index values

print("Reading csv file")
df=pd.read_csv("ThisisCSVfile.csv",index_col="name")
print(df)

