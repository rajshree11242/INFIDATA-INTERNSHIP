x=int(input("enter the total  no of  working days"))
y=int(input("enter the total no of days absent"))
a=y%x*100
b=100-a
if(b<=75):
    print("student is able to give the exam")
else:
    print("student is not able to give the exam")
print("end of the code")