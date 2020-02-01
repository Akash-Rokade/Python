mark=int(input("Enter mark"))
if(mark in range(0,40)):
    print("You fail")
elif(mark in range(40,100)):
    print("You pass")
else:
    print("provide valid")
