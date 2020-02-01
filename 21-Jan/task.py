import pymysql as con
db=con.connect("localhost",user="root",password="root",database="db")
cur=db.cursor()
query="select * from shop"
cur.execute(query)
data=cur.fetchall()
print(data)
temp=[]
temp=data
ch=0
while(ch<3):
    ch=int(input("\n1.Add to cart\n2.remove\nEnter Your choice"))
    if(ch==1):
        prod=input("Enter product to buy")
        for i in range (len(temp)):
            if(temp[i][1]==prod):
                print("Product available")
                s=temp[i]
                query="insert into cart values(0,%s,%s)"
                val=s[1:]
                #cur=db.cursor()
                cur.execute(query,val)
                db.commit()
                print("added to cart ")
    elif(ch==2):
        query="select * from cart"
        cur.execute(query)
        data1=cur.fetchall()
        print(data1)
        
        prod=input("Enter product to remove")
        for i in range(len(data1)):
             if(data1[i][1]==prod):
                 id1=data1[i][0]
                 query="delete from cart where idcart=%s"
                 val=[id1]
                 cur.execute(query,val)
                 db.commit()
                 break
        print("Deleted...")
db.close()
