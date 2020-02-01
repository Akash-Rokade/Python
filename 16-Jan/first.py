list=['a','b','c','d']
n=len(list)
for i in range (n):
    print(list[i])
list.remove('b')
n=n-1
print("after removing")
for i in range (n):
    print(list[i])
list.append(5)
n=n+1
print("after appending")
for i in range (n):
    print(list[i])
list.insert(2,'Akash')
n=n+1
print("after Inserting")
for i in range (n):
    print(list[i])
