def number():
    num = int(input("enter the number of student.."))
    name(num)

def name(num):
    i=1
  
    while i<=num:
     nam=input("enter name")
     sub_no=int(input("enter number of subject..."))
     subject(sub_no)
     i=i+1
    
    

def subject(sub):
    i=1
    a=0
    while i<=sub:
      sub_name=input("enter subject nameee..")  
      sub_marks=int(input("enter marks"))
      a=sub_marks+a
      i=i+1
    print(a)
 

    
number()
        