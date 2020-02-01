shop={}
ch=0
print("1.Add\n2.Remove\n3.Display key or value\n4.Check key to present\n5.Exit")
while(ch<6):
    ch=int(input("Enter Choice "))
    if(ch==1):
        k=input("Enter product name ")
        v=int(input("Enter Price "))
        shop[k]=v
    elif(ch==2):
        k=input("Enter product to remove ")
        shop.pop(k)
    elif(ch==3):
        new=int(input("Enter choice for 1.To Print Key\n2.To val"))
        if(new==1):
            key=shop.keys()
            print(key)
        elif(new==2):
            val=shop.values()
            print(val)
    elif(ch==4):
        k=input("ENter KEy to search")
        if k in shop.keys():
            print("Found")
        else:
            print("NOt Found")
print("Shopping: ",shop)
