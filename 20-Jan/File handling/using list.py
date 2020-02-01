f=open("writedata.txt","a")
l=["This is first\n","THis is third ","This is fourth\n"]
f.writelines(l)
f.close()
f=open("writedata.txt","r")
print("opening..")
print(f.read())
f.close()
