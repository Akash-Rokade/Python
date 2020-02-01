import pymysql as con
db=con.connect("localhost",user="root",password="root",database="db")
print("Connection succssfull")
query="insert into student values(%s,%s,%s,%s,%s)"
a=input("ENter name")
b=int(input("Enter Roll"))
c=int(input("Enter marks "))
d=input("Enter std ")
val=[0,a,b,b,d]
cur=db.cursor()
cur.execute(query,val)
db.commit()
print("data append successfull",val)
db.close()
