number=int(input("enterb the number..."))
number1=int(input("enterb the number..."))
c=(input("enter choice:"))
if c=='+':
    print("your addition is:",number+number1)
elif c=='-':
    print("your substrection is:",number-number1)
elif c=='*':
    print("your multiplication is:",number*number1)
elif c=='/':
    print("your division is:",number/number1)  
elif c=='**':
    print("your exponent is:",number**number1)
else:
    print("wrong input")
       
print("done")
