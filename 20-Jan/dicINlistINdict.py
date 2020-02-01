stud={}
ch=0
i=0
while(ch<4):
    ch=int(input("Enter Choice\n1.ADD\n2.remove\n3.Topper\n4.Exit"))
    sub=[]
    if(ch==1):
        
        roll=int(input("Enter Roll "))
        name=input("Enter Name")
        m1=int(input("Enter M1 Marks"))
        m2=int(input("Enter M2 Marks"))
        m3=int(input("Enter M3 Marks"))
        sub=[name,{"m1":m1,"m2":m2,"m3":m3}]
        
        stud[roll]=sub
        print(stud)  
    elif(ch==2):
        roll=int(input("Enter Roll to remove"))
        stud.pop(roll)
        print(stud)
        break
    elif(ch==3):
        sub=input("Enter Sub name\n->")
        high=0
        for key in stud.keys():
            if(high<stud[key][1][sub]):
                high=stud[key][1][sub]
        print(high)
        
