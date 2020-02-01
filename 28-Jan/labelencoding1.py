import pandas as pd
from sklearn.preprocessing import LabelEncoder
data={"shirtSize":["S","M","L","XL","XXL"],"Size":[36,38,40,42,44]}
df=pd.DataFrame(data)
print(df)
le=LabelEncoder()
le.fit(df.shirtSize)
print(le.classes_)#To show which classes we are encoding =['L','M','S','XL','XXL']
print(le.inverse_transform([2]))#it retrun specific class i.e-'S'
df.shirtSize=le.transform(df.shirtSize)
#print(df)
