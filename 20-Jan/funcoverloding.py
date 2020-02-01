def add(x,y):
    c=x+y
    print(c)
def add(x,y=2):
    c=x+y
    print(c)
a=int(input("Enter first"))
b=int(input("Enter second"))
add(a,b)
add(a)
