list=[]
a=int(input("enter number of element:"))
for i in range(a):
    ele=int(input())
    list.append(ele)
print(list)
sums=0
for i in list:
    sums=sums+i
print(sums)