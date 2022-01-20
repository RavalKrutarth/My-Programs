def maths():
    choice = int(input("enter choice.... 1. odd & EVen, 2. Factorial , 3. Prime number , 4. palindrome number"))
    if choice == 1:

        a = int(input("enter the number..."))
        if a %2==0:
           print("Even")
        else:
            print("Odd")
    elif choice ==2:
        b=int(input("enter the number.."))
        n=1
        for j in range(b,0,-1):
            n=n*j
        print("factorial of = ",b,"is = ",n)
    
    elif choice ==3:
        c=int(input("Enter number..."))
          
        if c==2 or c==3 or c==5 or c==7:
           print("Given number is Prime")
        
        elif c%2==0 or c%3==0 or c%5==0 or c%7==0 or c%11==0:
          print("not prime")
        
        else:
          print("primeeee")
    
    elif choice == 4 :
     number= int(input("enter the number..."))
     temp=number
     sum=0
     while number > 0:
         digit = number % 10
         sum = sum *10 + digit
         
         number =number//10
    
     if temp == sum:
      print("given number is palidrone...")  
     else :
      print("given number is not palidrone...")
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
def gst_bill():   
  a=int(input("ENTER NUMBER OF PRODUCTS....")) 
  i=0
  total=0
  h=int(input("Enter the percentage of gst..."))
  while i<a:
       product=int(input("ENTER PRODUCT PRICE:"))
       total=total+product
       i=i+1
  print("total price",total)
  gst=total*h/100
  c=total+gst
  print("TOTAL BILL INCLUDED GST....",c)
def game():

  import random
  no_tournament= int(input("enter how many times you want to play"))
  i=0
  win=0
  cowin=0
  while i <no_tournament:
         x=["STONE","PAPER", "SEIZOR"]
         a=random.choice(x)
         choice = input("Enter any STONE , PAPER , SEIZOR")
         if choice == "STONE" and a=="PAPER":
             cowin=cowin+1
             print("ROBOT CHOICE IS",a)
             print("YOU LOOSE")
         
         elif choice == "PAPER" and a=="SEIZOR":
             cowin=cowin+1
             print("ROBOT CHOICE IS",a)
             print("YOU LOOSE")
         
         elif choice == "SEIZOR" and a=="PAPER":
             cowin=cowin+1
             print("ROBOT CHOICE IS",a)
             print("YOU WIN")
         
         elif choice == "STONE" and a=="STONE": 
             print("ROBOT CHOICE IS",a)
             print("TIE MATCH")
         
         elif choice == "PAPER" and a=="PAPER":
             
             print("ROBOT CHOICE IS",a) 
             print("TIE MATCH")
         
         elif choice == "SEIZOR" and a=="SEIZOR":
              
              print("ROBOT CHOICE IS",a)
              print("TIE MATCH")
         
         elif choice== "STONE" and a=="SEIZOR":
             win=win+1
             print("COMPUTER CHOICE IS",a)
             print("you win..")
         
         elif choice== "PAPER" and a=="STONE":
             win=win+1
             print("COMPUTER CHOICE IS",a)
             print("you win..")
         
         elif choice== "SEIZOR" and a=="PAPER":
             win=win+1
             print("COMPUTER CHOICE IS",a)
             print("you win..")
         
         else:
             print("INVALID INPUT")
        
         i = i +1
  
  if cowin > win:
      print("you loose tournament..")
  elif  cowin < win:
      print("YOu win tournament")
  else:
      print("Tie match")      
    
         
    
 
         



choice = int(input("enter choice 1= maths function ,2 = student marksheet,3.GST BILL,4. Game"))

if choice ==1:
       maths()

elif choice == 2:
     student_marksheet()

elif choice == 3:
    gst_bill()
elif choice == 4:
    game()
