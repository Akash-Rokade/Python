s=5
n=s*2-1
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range (s-i):
            print(" ",end="")
        for k in range (mid+2+i+1):
            print("*",end=" ")
    print()
for i in range(n-1,0,-1):
        if(i<=mid):
            for j in range (s-i):
                    print(" ",end="")
            for k in range (mid+2+i+1):
                    print("*",end=" ")
        print()            

        
