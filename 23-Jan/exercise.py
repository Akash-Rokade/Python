import pandas as pd
df=pd.read_csv("pandas_task.csv",index_col="index")
'''print("First task")
print(df.head(5))
print(df.tail(5))

print("second task->Replace all blank with NaN ")
print(df.isna().sum())
#df=df.fillna('NaN')
#print(df)
print(df.loc[31])

print(df[df.price==df.price.max()])
print("question 4")
print(df.groupby("company").get_group('toyota'))
print("question 5")
print(df["company"].value_counts())
print("question 6")'''
print(df.groupby("company").price.max())
print("Question 7")


#df=df["average-mileage"].mean()
#print(df.groupby("company")["average-mileage"].mean())
print(df.sort_values("price",ascending=False).head(5))











            
