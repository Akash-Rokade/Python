list=[100,1,2,90,34,56,87,3,700]
n=len(list)
l=0
for i in range (n):
    for j in range(n):
        if(list[i]>list[j]):
            l=list[i]
            list[j]=list[i]
            list[i]=l
print(list[0])            
            
