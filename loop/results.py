a=int(input("how many students:"))
k=[]
l=[]
for i in range(a):
    b=(input("enter students name:"))
    c=int(input("enter no. of subject:"))
    l.append(b)
    sums=0
    for i in range(c):
        j=int(input("enter marks:"))
        sums=sums+j 
    print("total",sums)        
    k.append(sums)
print(k)
print(l)



