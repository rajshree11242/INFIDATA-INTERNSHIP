x=int(input("enter the age of the person"))
y=int(input("enter the no of days worked"))
gender=input("enter the gender of the person m/f")


wage=0
if(gender=='m' and x>=18 and x<30):
    wage=700*y
    print("wage of the male person", wage)
elif(gender=='f' and x>=18 and x<30):
    wage=750*y
    print("wage of the female person", wage)
elif(gender=='m' and x>=30 and x<=40):
    wage=800*y
    print("wage of the male person", wage)
else:
    wage=850*y
    print("wage of the female person",wage)

print("end of the code")

