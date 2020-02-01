n=int(input("ENter number"))
flag=0
for i in range(1,int(n/2)):
	if(n%i==0):
		print("This is prime")
		flag=1
if(flag==0):
	print("This is not prime")
