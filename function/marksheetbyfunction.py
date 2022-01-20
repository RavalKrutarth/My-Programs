
 




def mark_sheet():
    c = 0
    stu_num = int(input("enter the number of students..."))
    c= c + stu_num
    name_stu(stu_num)
    print(c)

def name_stu(stu_num):
     i = 0
     
     a=[]
     while i < stu_num :
         stu_name = input("enter student nameeee")
         no_subject = int(input("enter the number of subject..."))
         sub_name(no_subject)
         a.append(stu_name)
         
         i=i+1
     print(a)
     
    
def sub_name (no_subject):
    j=0
    b=[]
    while j < no_subject :
        subjectname=input("enter subject names....")
        b.append(subjectname)
        j=j+1
    
    print(b)
    return


mark_sheet ()