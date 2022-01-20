def number():
    num=int(input("enter number of students:"))
    name(num)
def name(num):
    i=1
    while i<=num:
        nam=input("enter name:")
        sub=int(input("enter number of subject:"))
        subject(sub)
        i=i+1
def subject(sub):
    i=1
    a=0
    while i<=sub:
        sub_name=input("enter name of subject:")
        sub_mark=int(input("enter marks.."))
        a=sub_mark+a
        print(a)
        i=i+1
    
number()


        