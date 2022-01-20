a=[9,0,'j','k']
b=[]
c=[]

for i in a:
    if type(i) == str :
        b.append(i)
    else:
        c.append(i)
    
print("int is",c)
print("string is",b)
