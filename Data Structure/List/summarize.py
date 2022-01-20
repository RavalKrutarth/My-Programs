element_list=int(input("enter the number of elemet lists that you want"))
i=1
a=[]
total=0
while i<= element_list:
    number=int(input("enter  numbersss"))
    a.append(number)
    total=total+number

    
    i=i+1

print(a)
print(total)