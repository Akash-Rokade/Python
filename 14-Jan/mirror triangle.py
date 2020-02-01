n=5
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(i+1):
            print("*",end=" ")
    else:
        for j in range (n-i):
             print("*",end=" ")
    print()
