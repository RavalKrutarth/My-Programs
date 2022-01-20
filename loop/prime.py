number=int(input("enter numberr.."))
if number%2==0:
    print(number,"is not prime")
elif number%3==0:
    print(number,"is not  prime")
elif number%5==0:
    print(number,"is  not prime")
elif number%7==0:
    print(number,"is not prime")
elif number%11==0:
    print(number,"is not prime")
else:
    print("given number is not prime")