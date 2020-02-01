import pymysql as con
db=con.connect("localhost",user="root",password="root",database="bank")
cur=db.cursor()
ch=0
while(ch<5):
        ch=int(input("\n1.Registration\n2.Login\n3.Update salary\nEnter Your choice"))
        if(ch==1):
            name=input("Enter name")
            email=input("Enter Email")
            password=input("Enter Password")
            balance=int(input("Enter Balance"))
            query="insert into user values(%s,%s,%s,%s,%s)"
            val=[0,name,email,password,balance]
            cur.execute(query,val)
            db.commit()
            print("Saved... ")
        elif(ch==2):
            name=input("Enter username")
            pass1=input("Enter pass")
            query="select * from user where name=%s and password=%s"
            val=[name,pass1]
            cur.execute(query,val)
            data=cur.fetchone()
            print(data) 
            if(data[1]==name and data[3]==pass1):
                print("\n\n\nHello",data[1])
                p=data[3]
                c=0
                while(c<5):
                    c=int(input("1.Credit\n2.Debit\n3.Chk bal\n4.Transfer\n4.logout"))
                    if(c==1):
                        cred=int(input("Money to credit\n->"))
                        query="update user set balance=balance+%s where password=%s"
                        val=[cred,pass1]
                        cur.execute(query,val)
                        db.commit()
                    elif(c==2):
                        deb=int(input("Enter amount to debt"))
                        query="update user set balance=balance-%s where password=%s"
                        val=[deb,pass1]
                        cur.execute(query,val)
                        db.commit()
                    elif(c==3):
                        query="select balance from user where password=%s"
                        val=[pass1]
                        cur.execute(query,val)
                        db.commit()
                        data=cur.fetchone()
                        print("User Balance ",data,"\n\n")
                   elif(c==4):
                       
                
            else:
                print("Invalid details")
        
