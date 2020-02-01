empid=[]
salary=[]
projects=[]
ch=0

print("1.Add")
print("2.Remove using empid")
print("3.Promotion using empid")
print("4.Promotion using no of project")
print("5.Exit")
while(ch<5):
    ch=int(input("Enter choice"))
    if(ch==1):
        eid=int(input("Enter Empid"))
        sal=int(input("Enter Salary"))
        project=int(input("Enter How many project he done"))
        empid.append(eid)
        salary.append(sal)
        projects.append(project)
    if(ch==2):
        print(empid)
        n=len(empid)
        rem=int(input("Enter Empid to remove"))
        for i in range (n):
            if(empid[i]==rem):
                empid.pop(i)
                salary.pop(i)
                projects.pop(i)
    if(ch==3):
        prom=int(input("Enter Empid to promotion"))
        n=len(empid)
        for i in range(n):
            if(empid[i]==prom):
                salary[i]+=500
        print(salary)
    if(ch==4):
        n=len(empid)
        for i in range (n):
            print(empid[i]," ",salary[i]," ",project[i])       
        
