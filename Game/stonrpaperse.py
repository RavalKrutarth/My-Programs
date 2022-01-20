import random
a=['stone','paper','sizor']
number=int(input("how many round you play:"))
comwin=0
userwin=0
for i in range(0,number):
    user1=(input("enter the choice:1)stone 2)paper 3)sizor:"))
    x=random.choice(a)

    if user1 == "stone" and x == "paper" or user1 == "paper" and x == "sizor" or user1 == "sizor" and x == "stone":
        print("computer choic:",x)
        print("you lost")
        comwin=comwin+1
    elif user1==x:
        print("computer choic:",x)
        print("tie")
    else:
        print("you win")
        userwin=userwin+1
if comwin>userwin:
    print("you lose the tourmant")
elif userwin>comwin:
    print("you win the tournmant")
