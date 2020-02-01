stud=[]
ch=0
while(ch<4):
    ch=int(input("Enter Choice\n1.Add\n2.Remove\n3.Topper\n4.Exit\n->"))
    if(ch==1):
        sub=[]
        marks=[]
        name=input("Enter student name\n->")
        roll=int(input("Enter student roll\n->"))
       
        sub.append(name)
        sub.append(roll)
        stud.append(sub)
        for i in range (3):
            m=int(input("Enter student amrks\n->"))    
            marks.append(m)
        sub.append(marks)
        print(stud)    
    
    elif(ch==2):
        roll=int(input("Enter roll number To remove\n->"))
        for i in range (len(stud)):
            if(stud[i][1]==roll):
                stud.pop(i)
            break
        print(stud)
    elif(ch==3):
        high1=[stud[0][2][0],stud[0][2][1],stud[0][2][2]]
        for i in range(1,len(stud)):
            for j in range (3):
                if (high1[j]<stud[i][2][j]):
                        high1[j]=stud[i][2][j]
                        
        print(high1)
                
            





    '''Simple ways
        n=int(input("ENter no of stud"))
        for i in range (n):
        name=input("")
        roll=input("Enter roll")
        m1=input("Enter frts marks")
        m2=input("Enter second maks")
        m3=input("Enter Thrisd maks")
        info=[name,roll,[m1,m2,m3]]
        stud.append(info)
      print(stud)  '''
        
