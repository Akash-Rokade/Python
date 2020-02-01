import pandas as pd
d={}
d["name"]=["abc","def","xyz"]
d["marks"]=[15,25,35]

df=pd.DataFrame(d).set_index("name")
print(df)

