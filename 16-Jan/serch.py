list=['a','b','c','d']
n=len(list)
flag=0
i=0
key=input("Enter key to search ")
for i in range(n):
    if(list[i]==key):
        print("Found")
        flag=1
        break

if(flag==0):
    print(" Not Found")
        
        
