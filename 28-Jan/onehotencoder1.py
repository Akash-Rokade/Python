import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data={"shirtSize":["S","M","L","XL","XXL"],"Size":[36,38,40,42,44]}
df=pd.DataFrame(data)
print(df)
ohe=OneHotEncoder()

data_ohr=ohe.fit_transform(df[['shirtSize']]).toarray()
print(data_ohr)
