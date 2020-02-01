stud=[]
marks=[]
topper=0
print("1.Add Student")
print("2.Remove Student")
print("3.Topper")
print("4.EXIT")
ch=0
while(ch<4):
    ch=int(input("Enter Choice"))
    if(ch==1):
        name=input("Enter Student name")
        mark=int(input("Enter Student Marks"))
        stud.append(name)
        marks.append(mark)
    elif(ch==2):
        name=input("Enter Student name to remove")
        n=len(stud)
        for i in range (n):
            if(stud[i]==name):
                stud.pop(i)
                marks.pop(i)
                break
    elif(ch==3):
        topper=max(marks)
        n=len(marks)
        for i in range (n):
            if (marks[i]==topper):
                print("Name of Topper",stud[i])
                print("Marks of Topper",topper)
    elif(ch==4):
        break
        
        
        
        
