import pymysql as con
db=con.connect("localhost",user="root",password="root",database="db")
query="UPDATE student SET name=%s WHERE idstudent=%s"
a=int(input("ENter id to update"))
b=input("Enter name to set")
val=[b,a]
cur=db.cursor()
cur.execute(query,val)
db.commit()
print("data updated",val)


query="select * from student where mark > 60"
cur.execute(query)
data=cur.fetchall()
print(data)

db.close()
