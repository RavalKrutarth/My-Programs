def one():
    number=int(input("Enter number of students.."))
    two(number)
    
def two(number):
    a=[]
    for i in range(0,number):
        name=input("enter name....")
        print(name)
        a.append(name)
    print(a)

    
      
one()

