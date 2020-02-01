import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data={"year":[1965,2010,1957,1925,1926],"age":[55,10,63,95,94]}
df=pd.DataFrame(data)

X=df[['year']]
Y=df[['age']]

xtrain,xtest,ytrain,ytest=train_test_split(X,Y)
LinearRegressor=LinearRegression()
LinearRegressor.fit(xtrain,ytrain)
ypred=LinearRegressor.predict([[20],[21]])
print(ypred)


