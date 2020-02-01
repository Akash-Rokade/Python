n=int(input("Enter number"))
m=n-1
for i in range (n):
    for m in range (m):
        print(" ",end="")
    for j in range (i+1):
        print("*",end=" ")
    print()   
