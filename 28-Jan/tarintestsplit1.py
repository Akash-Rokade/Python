import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv("titanic.csv")
x=df.drop(columns=['Survived'])
y=df.Survived
#print(x)
#print(y)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.35)
print("xtrain data\n",xtrain)
print("xtest data\n",xtest)
print("ytrain data\n",ytrain)
print("ytest\n",ytest)
