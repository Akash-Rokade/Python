import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("drinks_data.csv")
print(df)
beer_servings=df.beer_servings
spirit_servings=df.spirit_servings
wine_servings=df.wine_servings
total_litresof_pure_alcohol=df.total_litresof_pure_alcohol

#filling blank spaces using mean
df["beer_servings"]=df["beer_servings"].fillna(df["beer_servings"].mean())
df["spirit_servings"]=df["spirit_servings"].fillna(df["spirit_servings"].mean())
df["wine_servings"]=df["wine_servings"].fillna(df["wine_servings"].mean())
df["total_litresof_pure_alcohol"]=df["total_litresof_pure_alcohol"].fillna(df["total_litresof_pure_alcohol"].mean())

print(beer_servings)
print(spirit_servings)
print(wine_servings)
print(total_litresof_pure_alcohol)
data={"x":[1,2,3,4,5,6],"y":[5,6,7,8,9,3]}

df=pd.DataFrame(data)
x=df["x"]
y=df["y"]

print(x)
print(y)

xtrain,xtest,ytrain,ytest=train_test_split(x,y)
linearRegressor=LinearRegression()
linearRegressor.fit(xtrain,ytrain)

ypred=linearRegressor.predict(xtest)
print(ypred)


