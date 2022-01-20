v=['a','b','c',1,6,8,9]
integer=[]
string=[]
for i in v:
    if type(i)==int:
        integer.append(i)
    else:
        string.append(i)
print(integer)
print(string)  
    