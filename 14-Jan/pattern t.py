n=5
mid=int(n/2)
for i in range(n):
    if(i<=mid):
            for z in range (mid-i):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
    else:
        for z in range (i-mid):
                print(" ",end="")
        for j in range (n-i):
             print("*",end="")
    print()
