l=int(input("lenght"))
b=int(input("breadth"))
h=int(input("height"))

while(True):
    choice=int(input("enter your choice1:area,2:volume,3:exit"))
    if(choice==1):
        area=l*b
        print("area of rectangle:",area)
    elif(choice==2):
        vol=l*b*h
        print("volume of the cuboid:",vol)
    elif(choice==3):
        exit(0)
    else:
        print("invalid choice")