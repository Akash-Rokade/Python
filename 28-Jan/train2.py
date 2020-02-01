import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("pandas_task.csv")
x=df.drop(columns=['company'])
y=df.company
#print(x)
#print(y)

le=LabelEncoder()
le.fit(df.company)
print(le.classes_)#To show which classes we are encoding =['L','M','S','XL','XXL']
print(le.inverse_transform([2]))#it retrun specific class i.e-'S'
df.company=le.transform(df.company)
print(df.head(10))

