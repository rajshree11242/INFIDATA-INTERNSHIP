x=int(input("enter salary"))
y=int(input("enter years in the service"))

bonus=0

if(y>=10):
    b1=x+(x+10/100)
    print("bonus:",b1)
elif(y>=6 and y<=10):
    b2=x=(x+8/100)
    print("bonus:",b2)
else:
    b3=x+(x+5/100)
    print("bonus:",b3)