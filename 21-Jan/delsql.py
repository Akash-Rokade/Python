import pymysql as con
db=con.connect("localhost",user="root",password="root",database="db")
query="delete from student where idstudent=%s"
a=int(input("ENter id to delete"))
val=[a]
cur=db.cursor()
cur.execute(query,val)
db.commit()
print("data delete successfull",val)
db.close()
