list=[]
a=0
while(a<5):
    a=int(input("Enter choice 1.Insert 2.append 3.REmove 4.Exit"))
    if(a==1):
        n=int(input("Enter Index"))
        data=input("ENter data")
        list.insert(n,data)
    elif(a==2):
        list.append(input("ENter data"))
    elif(a==3):
        list.remove(input("Enter data to remove"))
    elif(a==4):
        a=5
print(list)        
    
