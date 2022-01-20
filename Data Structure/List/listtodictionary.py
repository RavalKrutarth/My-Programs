number=int(input("enter the no of students"))
i=1
sub_name=[]
k=[]
l=[]
while i<=number:
    name=input("enter the name")
    subject=int(input("Enter number of subjects:"))
    k.append(name)
    i=i+1
    j=1
    total=0
    while j<=subject:
        subname=input("enter the name of subjects:")
        marks=int(input("Enter the markssssss:"))

        total=total+marks
        sub_name.append(subname)
        j=j+1
    l.append(total)

print(k)       
print(sub_name)
print(l) 
z=dict(zip(k,l))
print(z)





