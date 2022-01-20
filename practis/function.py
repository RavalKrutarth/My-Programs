def odd_even():
    a=int(input("enter number:"))
    if a%2 == 0:
        s="even"
    else:
        s="odd"
    return s

def prime_number():
    a=int(input("enter number:"))
    if a==2 or a==3 or a==5 or a==7 or a==11:
        s="prime"
    elif a%2==0 or a%3==0 or a%5==0 or a%7==0 or a%11==0:
        s="not prime"
    else:
        s="prime"
    return s


def factorial():
    a=int(input("enter number:"))
    result=1
    for i in range(a,0,-1):
        result=result*i
    s=result
    return s
    
choice=int(input("enter number:"))
if choice==1:
    o=odd_even()
    print(o)
elif choice==2:
    a=prime_number()
    print(a)
elif choice==3:
    b=factorial()
    print(b)
else:
    print("error")