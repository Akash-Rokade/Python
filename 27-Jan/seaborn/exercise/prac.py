import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data_sample.csv",encoding='unicode_escape')
#print(df)


'''
#Example 1
month=df["MONTH_ID"]
mon=month.head(100)
sales=df["SALES"]
sal=sales.head(100)



x=[]
y=[]
x=mon
y=sal
plt.plot(x,y,color='R',marker='*')
plt.title("LinePlot Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


#Example 2
month=df["MONTH_ID"]
mon=month.head(50)
sales=df["SALES"]
sal=sales.head(50)


x=[]
y=[]
x=mon
y=sal
plt.plot(x,y,color='R',marker='o',markersize=9,linestyle='--',linewidth=3,label='Profit data of last year')
plt.title("LinePlot Graph")
plt.xlabel("Month Number")
plt.ylabel("Sales or Price")
plt.legend(loc='lower right')
plt.show()

#example 3

#pd=df["PRODUCTLINE"]
#pd=pd.head(100)
df=df.head(100)
motor=df.groupby("PRODUCTLINE").get_group('Motorcycles')
classic=df.groupby("PRODUCTLINE").get_group('Classic Cars')


month=motor["MONTH_ID"]
mon=month.head(100)
sales=motor["SALES"]
sal=sales.head(100)

month1=classic["MONTH_ID"]
mon1=month1.head(100)
sales1=classic["SALES"]
sal1=sales1.head(100)



x=[]
y=[]
x1=[]
y1=[]
x=mon
y=sal
x1=mon1
y1=sal1

plt.plot(x,y,label='MotorCycle sales Data')
plt.plot(x1,y1,label='Classic cars sales data')

#plt.plotline(x,y,color='R',marker='o',label='Motorcycle sales Data')
plt.title("LinePlot Graph")
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.legend()
plt.show()
#example 4
motor=df.groupby("PRODUCTLINE").get_group('Motorcycles')
month=motor["MONTH_ID"]
mon=month.head(100)
sales=motor["SALES"]
sal=sales.head(100)



x=[]
y=[]
x=mon
y=sal
plt.scatter(x,y,marker='o')
plt.title("scatterPlot Graph")
plt.xlabel("Month Number")
plt.grid(linestyle='--')
plt.ylabel("Number of unit sales")
plt.show()'''

#example 5




