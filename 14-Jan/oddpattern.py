n=6
m=n
for i in range(n):
    for j in range (i+1):
        print(" ",end="")
    for k in range (n-j-2):
        print("*",end="")
    print()


