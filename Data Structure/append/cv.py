c=[2,3,4,5,7,8,9]
v=[2,3,4,8,7,5]

a=[]

for i in c:
    if i not in v:
        a.append(i)
        

print(a)