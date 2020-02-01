marks=int(input("Enter amrks"))
if(marks<0):
    print("Enter positive mark")
elif(marks<40):
    print("Your Fail")
elif(marks>=40 and marks<50):
   print("You pass")
elif(marks>=50 and marks<60):
   print("Your in third class")
elif(marks>=60 and marks<70):
   print("Your in second class")
elif(marks>=70 and marks<80):
   print("You in first class")
elif(marks>=80 and marks<100):
   print("Your in Destinction")
else:
   print("provide Valid input")
