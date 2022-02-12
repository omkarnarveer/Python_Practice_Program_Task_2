#Function for Area
def Tr_Area():
    b=float(input("Enter Base: "))
    h=float(input("Enter Height: "))
    a=0.5*b*h
    print("Area of Triangle is ",a)
    return a
 #Function for Perimeter   
def Tr_Perimeter():
    s1=float(input("Enter Side 1: "))
    s2=float(input("Enter Side 2: "))
    s3=float(input("Enter Side 3: "))
    p=s1+s2+s3
    print("Perimeter of Triangle is ",p)
    return p
