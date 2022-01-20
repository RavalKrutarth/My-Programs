list=[]
a=int(input("enter number of element:"))
for i in range(a):
    ele=int(input())
    list.append(ele)
k=int(input("enter number multipal you want:"))
list2=[]
for i in list:
    if i%k==0:
        list2.append(i)
        print(list2)
    else:
        print("no multipal.")
    

     