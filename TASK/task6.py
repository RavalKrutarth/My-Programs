list=[]
a=int(input("enter element:"))
for i in range(a):
    number=int(input("enter number:"))
    list.append(number)
evenlist=[]
oddlist=[]
for j in list:
    if j%2==0:
        evenlist.append(j)
    else:
        oddlist.append(j)
print("even number:",evenlist)
print("odd number:",oddlist)


        