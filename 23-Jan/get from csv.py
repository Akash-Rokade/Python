import pandas as pd
df=pd.read_csv("book1.csv",index_col="Roll")
print(df)
'''print("To find blank field")
print(df.isna().sum())


df["Age"]=df["Age"].fillna(df["Age"].mean())#To Fill blank with mean()
print(df)
df["Age"]=df["Age"].astype("int")
print(df)
df=df.fillna(0)#To Fill the blank with 0
print(df)
print(df.isna().sum())
print(df.info())
print(df.columns)
print(df.drop(columns=["Age"]))
print(df.head(3))
print(df.dropna())
print(df.loc[2])
print(df.iloc[0:1:,1:2])

print(df["Age"].value_counts())#print how many time each value repeated
print(df[df["M1"]>70])
print(df.groupby("Age").get_group(21))'''
print(df.sort_values("Age",ascending=False))
df["Age"]=df["Age"].replace(21,18)
print(df)

japancars={'company':['Ford','Mercedes','BMW','Audi'],'price':[23845,171995,135925,71400']}
germancars={'company':['Toyota','Honda','Nissan','Mitsubishi'],'price':[29995,23600,61500,58900']}
rs=concate(japancars,germancars)
print(rs)
