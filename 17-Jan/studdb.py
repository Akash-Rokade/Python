stud=[]
sub=[]
n=int(input("How Many Number You want To enter\n->"))
for i in range (n):
    sub=[]

    name=input("Enter Student name\n->")
    roll=int(input("Enter Student Roll no\n->"))
    mark=int(input("Enter Student MArk\n->"))
    sub.append(name)
    sub.append(roll)
    sub.append(mark)
    stud.append(sub)
print(stud)
top=stud[0][2]
for i in range (len(stud)):
        if(stud[i][2]>top):
           top=stud[i][2]
           name=stud[i][0]
print("Topper Name:",name,"score.:",top)
