print("Pattern")
n=int(input("Enter Number"))
m=n-1
for i in range (n):
    
    for i in range (0,m):
        print(" ",end="")
    for s in range (n+1):
        print("*",end="")
        m=m-1
    
