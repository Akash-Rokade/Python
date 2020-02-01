import pymysql as con
db=con.connect("localhost",user="root",password="root",database="empdb")
cur=db.cursor()
ch=0
while(ch<4):
    ch=int(input("\n1.Add Employee\n2.remove employee\n3.Update salary\nEnter Your choice"))
    if(ch==1):
        ename=input("Enter Emp name")
        esal=int(input("Enter emp sal"))
                
        query="insert into emp values(%s,%s,%s)"
        val=[0,ename,esal]
        cur.execute(query,val)
        db.commit()
        print("Saved... ")
    elif(ch==2):
        query="select * from emp"
        cur.execute(query)
        data1=cur.fetchall()
        print(data1)
        
        rem=input("Enter emp name to remove")
        for i in range(len(data1)):
             if(data1[i][1]==rem):
                 id1=data1[i][0]
                 query="delete from emp where idemp=%s"
                 val=[id1]
                 cur.execute(query,val)
                 db.commit()
                 break
        print("Deleted...")
    elif(ch==3):
       
       id=int(input("Enter id "))
       sal=int(input("Enter sal to increment"))
       query="update emp set sal=sal+%s where idemp=%s"
       val=[sal,id]
       cur.execute(query,val)
       db.commit()
       print("updated..")
db.close()
