age=int(input("Enter age"))
gender=input("Enter Gender [m OR f]")
if(age>=21 and gender=="m"):
        print("Your are male over 21")
elif(age>=18 and gender=="f"):
        print("You are female over 18")
else:
    print("You are not eligible")
        
