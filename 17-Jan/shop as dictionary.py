shop={'oil':10,'milk':20,'rice':30}
cart={}
ch=0
bill=0
print("1.Add\n2.REmove\n3.Bill\n4.Exit")
while(ch<4):
    ch=int(input("Enter Your choice"))
    if(ch==1):
        k=input("ENter Prod name\n")
        if k in shop:
              cart[k]=shop[k]
        print("Your Cart",cart)         
    elif(ch==2):
        k=input("ENter Product as key To Remove")
        cart.pop(k)
        print(cart)
    elif(ch==3):
        for b in cart.values():
            bill=bill+b
        print("Total.:",bill)   
