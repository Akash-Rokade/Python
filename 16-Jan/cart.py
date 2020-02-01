item=['pizza','burger','dosa','milk','egg']
price=[90,50,30,60,40]
cart=[]
n=len(item)
total=0
ch=0
print("*******Menu*********")
print("index  Item Price")
for i in range (n):
    print(i+1,".",item[i],"  ",price[i])
print("99 for add to cart ")
print("00 for total ")
while(i<6):
    ch=int(input("Enter choice "))
    if(ch==99):

            buy=int(input("Enter index to add cart "))
            buy=buy-1
            p=price[buy]
            cart.append(p)
            print(cart)
    elif(ch==00):
        g=len(cart)
        for i in range (g):
            total=total+cart[i]
        break    

print(total)




