n=8
for i in range (n):
    for j in range (n):
        if(j==0 or j==n-1 or i==0 or i==n-1 or i==j ):
            print("*",end="")
        else:
            print(" ",end="")
    print()
