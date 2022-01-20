class ATM():
    def balance(self,a):
        self.a=a
        return self.a
    def deposite(self):
        d=int(input("enter deposite amount:"))
        self.a+=d
        return self.a
    def withdraw(self):
        k=int(input("enter withdraw amount:"))
        self.a-=k
        return self.a
x=ATM()
n=int(input("set the balance amount:"))
print(x.balance(n))
b=int(input("set the passoword:"))
mo_num=int(input("enter mobile number:"))

trial=3

while True:
    pin=int(input("enter the pin:"))
    if pin==b:
        choice=int(input("1)set pin 2)diposite amount 3)withdraw amount 4)exit"))

        if choice==1:
                while True:                                       
                    current_pin=int(input("enter the pin:"))
                    if b==current_pin:
                        print("ok")
                        break
                    else:
                        trial=trial-1
                        if trial==0:
                            print("your card is block")
                            break
                        else:
                            print("you left",trial,"trial")
                            print("INVALID PIN...")


        elif choice==2:
            while True:
                pin=int(input("enter the pin:"))
                if pin==b:
                    print("updated balance=",x.deposite())
                    break
                else:
                    trial=trial-1
                    if trial==0:
                        print("your card is block")
                        break
                    else:
                        print("you left",trial,"trial")
                        print("invalid pin...")
        

        elif choice==3:
            while True:
                pin=int(input("enter the pin:"))
                if pin==b:
                    print("updated balance=",x.withdraw())
                    break
                else:
                    trial=trial-1
                    if trial==0:
                        print("your card is block")
                        break
                    else:
                        print("you left",trial,"trial")
                        print("invalid pin...")
        elif choice==4:
            break
        else:
            print("INVALID...")

    else:
        trial=trial-1
        if trial==0:
            print("your card is block")
            break
        else:
            print("you left",trial,"trial")
                               


    



    



