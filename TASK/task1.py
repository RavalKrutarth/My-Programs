list=[]
list2=[]
a=int(input("enter number of element:"))
for i in range(a):
    ele=input()
    list.append(ele)
print(list)
for i in list:
    k=i[0:][-1]
    list2.append(k)
print(list2)

