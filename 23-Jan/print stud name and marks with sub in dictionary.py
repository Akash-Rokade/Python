import pandas as pd
dic={'M1':[1,2,7,5],'M2':[3,4,8,9],'M3':[5,6,3,2],'ESIOT':[7,8,1,0]}
df=pd.DataFrame(dic,index=["Stud1","Stud2","Stud3","Stud4"])
#print(df["ESIOT"]["Stud3"])
print(df[df.ESIOT==df.ESIOT.max()])
#print(max(df.ESIOT.index))


