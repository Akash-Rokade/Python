l={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
for a in l.keys():
    print(a,l[a])
for val in l.values():
    print(val)
for item in l.items():
    print(item[0],item[1])
for val,key in l.items():
    print(val,key)
