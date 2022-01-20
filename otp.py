import random
a='1234567890'

while True:
       mo_num=(input("enter your mobile nnumber:"))
       lenght=len(mo_num)
       if lenght==10:
              b=random.sample(a,4)
              print(" ".join(b))
              break

       else:
              print("invalid number..")
              