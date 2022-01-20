i=1
c=input("which categery:")
if c=="Electronics":
    p=int(input("no. of product:"))
    sums=0
    while i<=p:
        j=input("enter product name:")
        v=int(input("enter price:"))
        sums=sums+v
        i=i+1
       
    f=int(input("how many you need discount:"))
    print("total",sums)
    gst=(sums*f)/100
    print("gst",gst)
    total=gst+sums
    print("grant total",total)

    
elif c=="Glossary":
    k=int(input("no. of product:"))
    sums=0
    while i<=k:
        j=input("enter product name:")
        v=int(input("enter price:"))
        sums=sums+v
        i=i+1
    f=int(input("how many you need discount:"))   
    print("total",sums)
    gst=(sums*f)/100
    print("gst",gst)
    total=gst+sums
    print("grant total",total)


