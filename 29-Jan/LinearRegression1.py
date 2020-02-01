import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=pd.read_csv("winequality-red.csv",sep=";")

#data={"year":[1965,2010,1957,1925,1926],"age":[55,10,63,95,94]}
df=pd.DataFrame(data)
print(df)

y=df.quality
X=df.drop('quality',axis=1)
print("OTHER********",X,"QUALITY********",y)
xtrain,xtest,ytrain,ytest=train_test_split(X,y)
LinearRegressor=LinearRegression()
LinearRegressor.fit(xtrain,ytrain)
ypred=LinearRegressor.predict([[xtest]])
print(ypred)

'''
df["beer_servings"]=df["beer_servings"].fillna(df["beer_servings"].mean())
df["total_litresof_pure_alcohol"]=df["total_litresof_pure_alcohol"].fillna(df["total_litresof_pure_alcohol"].mean())
X=df["beer_servings"]
Y=df["total_litresof_pure_alcohol"]


xtrain,xtest,ytrain,ytest=train_test_split(X,Y)
LinearRegressor=LinearRegression()
LinearRegressor.fit(xtrain,ytrain)
ypred=LinearRegressor.predict([[4.9]])
print(ypred)'''
