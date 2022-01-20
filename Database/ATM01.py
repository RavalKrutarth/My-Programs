import sqlite3
dot=[]
Got=[]
def connection():
    a=sqlite3.connect("ATM.db")
    return a
def create_tb(a):
    a.execute('''CREATE TABLE IF NOT EXISTS ATM(ACCOUNT INTEGER  PRIMARY KEY, NAME TEXT,PASSWORD INT,AMOUNT INT)''')

def insert_tb(a):
    k=int(input("Enter number of people:"))
    for i in range(k):
        acc_no=int(input("Enter account number:"))
        name=input("Enter Name:")
        Pin=int(input("Enter PIN number:"))
        amount=int(input("Enter Amount:"))
        print("Acount Created...")
        a.execute("INSERT INTO ATM(ACCOUNT,NAME,PASSWORD,AMOUNT) VALUES(?,?,?,?)",(acc_no,name,Pin,amount))
        return a
def retrieve(a):
    cursor = a.cursor()
    id=int(input("Reenter your Ac Number:"))
    user=int(input("Reenter your pin:"))
    dot.append(id)
    B1="SELECT * FROM ATM WHERE ACCOUNT=?"
    A1="SELECT * FROM ATM WHERE PASSWORD=?"
    if A1 and B1:
        cursor.execute(A1,(user,))
        cursor.execute(B1,(id,))
        rows= cursor.fetchall()
    for row in rows:
        continue
    if row[0]==id and row[2]==user:
        print("**\twelcome to online atm :)")
        class atm():
            def amount(self,a):
                self.a=a
                return self.a
            def deposit(self,b):
                self.b=b
                self.a=self.a+self.b
                return self.a
            def withdraw(self,c):
                self.c=c
                if self.a>=c:
                    self.a=self.a-self.c
                else:
                    print("insuficient balance :")
                return self.a
            def finalamount(self):
                return self.a

        x=atm()
        n=row[3]
        print(x.amount(n))
        while True:
            print("\n1 --> deposit")
            print("2 --> withdraw")
            print("3 --> exit")
            z=int(input("Please enter 1 or 2 or 3 :"))
            if z==1:
                nn=int(input("Enter Amount To Deposit :"))
                print(x.deposit(nn))
            elif z==2:
                nnn=int(input("Enter Amount To Withdraw :"))
                print("Remaining Balance :",x.withdraw(nnn))
            elif z==3:
                print("Final Balance in your Account :",x.finalamount())
                Got.append(x.finalamount())
                break
            else:
                break
    
    else:
        print("\tData Match Not Found :(")
        print("<<< Try Again >>>")
        retrieve(a)

def update(a):
    cursor=a.cursor()
    hq=dot[0]
    fc=Got[0]
    zef="UPDATE ATM04 SET AMOUNT=? WHERE ACCOUNT=?"
    cursor.execute(zef,(fc,hq))
    
obj= connection()
create_tb(obj)
A1 = insert_tb(obj)
retrieve(obj)
update(obj)
obj.commit()
obj.close()
