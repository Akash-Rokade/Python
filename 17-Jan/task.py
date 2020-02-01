shop=[['oil',10],['milk',20],['egg',30]]
cart=[]
bill=0
print("1.Add To cart")
print("2.Remove from cart")
print("3.Bill")
print("4.Exit")
ch=0
while(ch<4):
    print("Our Products",shop)
    ch=int(input("ENter Choice\n->"))
    if(ch==1):
        buy=input("Enter Product Name\n->")
        for i in range (len(shop)):
                if(shop[i][0]==buy):
                    rec=shop[i]
                    cart.append(rec)
                    print("Added to cart ",cart)
                    print()
                    print()
    elif(ch==2):
        p=0
        rem=(input("Enter Prod name to remove"))
        for i in range (len(cart)):
                    if(cart[i][0]==rem):
                        #p=i
                        cart.pop(p)
                        break
        print("Available cart.:",cart)           
    elif(ch==3):
        for i in range (len(cart)):
            bill=bill+cart[i][1]
        print("Final Bill,:",bill)   
