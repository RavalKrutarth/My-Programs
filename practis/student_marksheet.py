def student_marksheet():
    no_student=int(input("enter the number of students.."))
    i=0
    
    b=[]
    c=[]
    d=[]
    e=[]
    while i < no_student:
        name= input("enter name....")
        b.append(name)
        print("enter subject that has ", name ,"has choosen")
        number_subject = int(input())
        k=0
        total=0
        while k < number_subject:
                name_subject = input("enter the subject name...")
                print("enter the marks of",name_subject)
                marks_subject=int(input(" "))
                total= marks_subject + total
                d.append(marks_subject)
                c.append(name_subject)
                k=k+1
                e.append(total)
                i=i+1
    
        print("name  = ",b)
        print("subject name =",c)
        print("marks =",d)
        print("total",e)

        
def maths():
    a=int(input("enter number:"))
    if a%2==0:
            print("even")
    else:
            print("odd")

def factorial():
        a=int(input("enter number:"))
        result=1
        
        for i in range(a,0,-1):
               result=result*i
               s=result
               
        
        
        return s


def stonpaper():
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

def gst():
    a=200
    g=10
    gst=(a*g)/100
    print(gst)

    total=gst+a
    print(total)

def employersinfo():
        a=(input("Which department:"))
        incriment=int(input("how many incriment you want:"))
        
        if a =="it department":
                p=int(input("no. of employ:"))
                for i in range(p):
                     j=(input("employe name:"))
                     k=int(input("enter salary:"))
                     c=k*incriment/100
                     b=k+c
                     print("name",j,"\nold salary",k,"\nsalary with incriment",b) 
        else :
             print("ERROR")









b=int(input("1=student,2=maths,3=factorial,4=game,5=gst,6=employerinfo"))
if b==1:
        student_marksheet()
elif b==2:
        maths()
elif b==3:
       b= factorial()
       print(b)
elif b==4:
        stonpaper()
elif b==5:
        gst()
elif b==6:
        employersinfo()
else:
        print("error")
